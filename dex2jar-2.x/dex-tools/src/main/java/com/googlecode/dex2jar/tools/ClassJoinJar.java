package com.googlecode.dex2jar.tools;

/**
 * Created by Administrator on 2017/2/22.
 */
/*
 * dex2jar - Tools to work with android .dex and java .class files
 * Copyright (c) 2009-2012 Panxiaobo
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */


import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.nio.file.FileSystem;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Enumeration;
import java.util.zip.ZipEntry;
import java.util.zip.ZipFile;
import java.util.zip.ZipOutputStream;

@BaseCmd.Syntax(cmd = "d2j-class-join-jar", syntax = "[options] <dir>", desc = "Add class into jar.")
public class ClassJoinJar extends BaseCmd {
    @Opt(opt = "f", longOpt = "force", hasArg = false, description = "force overwrite")
    private boolean forceOverwrite = false;
    @Opt(opt = "i", longOpt = "into", description = "input .jar file", argName = "the-jar-file")
    private Path into;
    @Opt(opt = "o", longOpt = "output", description = "output .jar file", argName = "the-jar-file")
    private Path output;
    @Opt(opt = "d", longOpt = "debug", hasArg = false, description = "debug", argName = "debug")
    private boolean debug = false;
    @Opt(opt = "p", longOpt = "packagename", description = "package name", argName = "package-name")
    private String packagename;

    public static void main(String... args) {
        new ClassJoinJar().doMain(args);
    }

    private boolean addFileToZipFile(String fileName, String jarFileName, String newJarFileName, String mPackageName) {
        try {
            System.err.println("---------------------------");
            System.err.println("FileInputStream" + fileName);
            System.err.println(jarFileName);
            System.err.println(newJarFileName);
            System.err.println(mPackageName);
            FileInputStream fis = new FileInputStream(fileName);
            ByteArrayOutputStream bos = new ByteArrayOutputStream();
            int len = 0;
            byte[] buffer = new byte[1024];
            while ((len = fis.read(buffer)) > 0) {
                bos.write(buffer, 0, len);
            }
            ZipFile war = new ZipFile(jarFileName);
            ZipOutputStream append = new ZipOutputStream(new FileOutputStream(newJarFileName));
            Enumeration<? extends ZipEntry> entries = war.entries();
            int count;
            byte[] data = new byte[1024];
            while (entries.hasMoreElements()) {
                ZipEntry e = entries.nextElement();
                if (debug)
                    System.err.println("Entry: " + e.toString());
                InputStream in = war.getInputStream(e);
                append.putNextEntry(e);
                if (!e.isDirectory()) {
                    while ((count = in.read(data, 0, 1024)) != -1) {
                        append.write(data, 0, count);
                    }
//                    append.flush();
                }
                append.closeEntry();
            }
            int index = fileName.lastIndexOf(File.separator);
            String s = fileName.substring(index + 1);
            s = mPackageName.replace('.', '/') + File.separator + s;
            if (debug)
                System.err.println("Join Entry: " + s);

            ZipEntry e = new ZipEntry(s);

            //ZipOutputStream in = new ZipOutputStream(new FileOutputStream(zipFileName));
            append.putNextEntry(e);
            append.write(bos.toByteArray());
            append.closeEntry();
            war.close();
            append.close();

            return true;
        } catch (Exception e) {
            e.printStackTrace();
            return false;
        }
    }

    //// ..\tmp\no1\Programmer.class         ..\tmp\no1\no1.jar
    private boolean addClassFileToJar(String classFilePath, String jarName, String newJarName, String packagename) {
        try {
//            int index = jarName.lastIndexOf(".");
//            String path = jarName.substring(0, index);
//            String spath = jarName.substring(index);
//            System.err.println("path:" + path);
//            System.err.println("spath:" + path + "-tmp" + spath);
            File oldZipFile = new File(jarName);
            File newZipFile = new File(newJarName);
            addFileToZipFile(classFilePath, oldZipFile.getAbsolutePath(), newZipFile.getAbsolutePath(), packagename);
            //oldZipFile.delete();
            //newZipFile.renameTo(oldZipFile);
            return true;
        } catch (Throwable e) {
            return false;
        }
    }

    @Override
    protected void doCommandLine() throws Exception {
        if (remainingArgs.length != 1) {
            usage();
            return;
        }

        Path cls = new File(remainingArgs[0]).toPath();
        System.err.println("zj " + cls.toString());//..\tmp\no1\Programmer.class
        if (!Files.exists(cls)) {
            System.err.println(cls + " is not exists");
            usage();
            return;
        }

        if (packagename == null) {
            packagename = "com.example";
        }

        if (into == null) {
            if (Files.isDirectory(cls)) {
                into = new File(cls.getFileName() + "-into.jar").toPath();
            } else {
                into = new File(cls.toString() + "-into.jar").toPath();
            }
        }

        if (output == null) {
            if (Files.isDirectory(cls)) {
                output = new File(cls.getFileName() + "-out.jar").toPath();
            } else {
                output = new File(cls.toString() + "-out.jar").toPath();
            }
        }

        if (Files.exists(into) && !forceOverwrite) {
            System.err.println(into + " exists, use --force to overwrite");
            usage();
            return;
        }

        Path tmp = null;
        final Path realJar;
        try {
            if (Files.isDirectory(cls)) {
                realJar = Files.createTempFile("d2j", ".cls");
                tmp = realJar;
                System.out.println("zipping " + cls + " -> " + realJar);
                try (FileSystem fs = createZip(realJar)) {
                    final Path outRoot = fs.getPath("/");
                    walkJarOrDir(cls, new FileVisitorX() {
                        @Override
                        public void visitFile(Path file, String relative) throws IOException {
                            if (file.getFileName().toString().endsWith(".class")) {
                                Files.copy(file, outRoot.resolve(relative));
                            }
                        }
                    });
                }
            } else {
                realJar = cls;
            }

            System.out.println("class join jar " + realJar + " and " + into + "->" + output);
            System.out.println("packagename:" + packagename);
            //jar2dex ..\tmp\no1\Programmer.class -> ..\tmp\no1\no1.jar
            addClassFileToJar(realJar.toString(), into.toString(), output.toString(), packagename);

        } finally {
            if (tmp != null) {
                Files.deleteIfExists(tmp);
            }
        }

    }
}


