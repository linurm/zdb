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


import java.io.BufferedReader;
import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStream;
import java.nio.file.FileSystem;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.Enumeration;
import java.util.List;
import java.util.zip.ZipEntry;
import java.util.zip.ZipFile;
import java.util.zip.ZipOutputStream;

@BaseCmd.Syntax(cmd = "d2j-class-update-jar", syntax = "[options] <dir>", desc = "Add class update into jar.")
public class ClassUpdateToJar extends BaseCmd {
    List<String> list_class = new ArrayList<String>();
    @Opt(opt = "f", longOpt = "force", hasArg = false, description = "force overwrite")
    private boolean forceOverwrite = false;
    @Opt(opt = "i", longOpt = "into", description = "input .jar file", argName = "the-jar-file")
    private Path into;
    @Opt(opt = "o", longOpt = "output", description = "output .jar file", argName = "the-jar-file")
    private Path output;
    @Opt(opt = "d", longOpt = "debug", hasArg = false, description = "debug", argName = "debug")
    private boolean debug = false;
    @Opt(opt = "p", longOpt = "path", description = "path .class file", argName = "the-class-file")
    private Path classpath;


    public static void main(String... args) {
        new ClassUpdateToJar().doMain(args);
    }

    private boolean addFileToZipFile(String jarFileName, String newJarFileName) {
        try {

            //System.err.println(classFileName);
            if (debug) {
                System.err.println(jarFileName);
                System.err.println(newJarFileName);
            }
//            System.err.println(mPackageName);
            //FileInputStream fis = new FileInputStream(classFileName);
            ByteArrayOutputStream bos = new ByteArrayOutputStream();
//            int len = 0;
//            byte[] buffer = new byte[1024];
//            while ((len = fis.read(buffer)) > 0) {
//                bos.write(buffer, 0, len);
//            }
            ZipFile war = new ZipFile(jarFileName);
            ZipOutputStream append = new ZipOutputStream(new FileOutputStream(newJarFileName));
            Enumeration<? extends ZipEntry> entries = war.entries();
            FileInputStream fis;
            int count;
            int index;
            int len;
            byte[] data = new byte[1024];
            while (entries.hasMoreElements()) {
                ZipEntry e = entries.nextElement();
                if (debug)
                    System.err.println("Entry: " + e.toString());
                InputStream in = war.getInputStream(e);

                if (!e.isDirectory()) {
                    if (isModefy(e) == 1) {
//                        String s = e.toString();
//                        index = s.lastIndexOf("/");
//                        String classname = classpath.toString() + File.separator + s.substring(index + 1);
//                        //xx/xx/xx.class
//                        System.err.println("classname: " + classname);
//                        System.err.println("Update: " + s);
//                        String class_path = new File(classname).getAbsolutePath();
//                        System.err.println("class_path: " + class_path);
//                        fis = new FileInputStream(classname);
//
//                        ZipEntry e1 = new ZipEntry(s);
//                        append.putNextEntry(e1);//
//                        while ((len = fis.read(data)) > 0) {
//                            bos.write(data, 0, len);
//
//                        }
//                        append.write(bos.toByteArray());
//                        append.closeEntry();
//                        fis.close();
//                        if (debug)
//                            System.err.println(class_path);
                        ;
                    } else {
                        append.putNextEntry(e);
                        while ((count = in.read(data, 0, 1024)) != -1) {
                            append.write(data, 0, count);
                        }
                        append.closeEntry();
                    }
//                    append.flush();
                } else {
                    append.putNextEntry(e);
                    append.closeEntry();
                }
//                append.closeEntry();
            }
            for (String attribute : list_class) {
                //updateClasses();
                String s = attribute;
//                String s = e.toString();
                index = s.lastIndexOf("/");
                String classname = classpath.toString() + File.separator + s.substring(index + 1);
                //xx/xx/xx.class
                System.err.println("FileInputStream: " + classname);
                System.err.println("Update: " + s);
                String class_path = new File(classname).getAbsolutePath();
                System.err.println("class_path: " + class_path);
                try {
                    fis = new FileInputStream(classname);
                } catch (Exception e) {
                    if (debug)
                        System.err.println("something wrong, but do not worry!!! maybe the file is not exist!!!");
                    continue;
                }

                while ((len = fis.read(data)) > 0) {
                    bos.write(data, 0, len);
                }
                ZipEntry e1 = new ZipEntry(s);
                append.putNextEntry(e1);//
                append.write(bos.toByteArray());
                append.closeEntry();
                fis.close();
                if (debug)
                    System.err.println("test: " + class_path);
                ;
            }
//            int index = classFileName.lastIndexOf(File.separator);
//            String s = classFileName.substring(index + 1);
//            s = mPackageName.replace('.', '/') + '/' + s;
//            if (debug)
//                System.err.println("s:" + s);
//            ZipEntry e = new ZipEntry(s);
//            append.putNextEntry(e);
//            append.write(bos.toByteArray());
//            append.closeEntry();
            war.close();
            append.close();

            return true;
        } catch (Exception e) {
            e.printStackTrace();
            return false;
        }
    }

    //// ..\tmp\no1\Programmer.class         ..\tmp\no1\no1.jar
    private boolean addClassFileToJar(String jarName, String newJarName) {
        try {
//            int index = jarName.lastIndexOf(".");
//            String path = jarName.substring(0, index);
//            String spath = jarName.substring(index);
//            System.err.println("path:" + path);
//            System.err.println("spath:" + path + "-tmp" + spath);
            File oldZipFile = new File(jarName);
            File newZipFile = new File(newJarName);
            addFileToZipFile(oldZipFile.getAbsolutePath(), newZipFile.getAbsolutePath());
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
        System.err.println("list file " + cls.toString());//..\tmp\no1\Programmer.class
        if (!Files.exists(cls)) {
            System.err.println(cls + " is not exists");
            usage();
            return;
        }

        if (readClassList(cls.toString()) != 0) {
            usage();
            return;
        }
        //return;


        Path tmp = null;
        try {
            System.out.println("class update " + into + " --> " + output);
            addClassFileToJar(into.toString(), output.toString());
        } finally {
            if (tmp != null) {
                Files.deleteIfExists(tmp);
            }
        }

    }

    public int isModefy(ZipEntry entry) {
        //System.out.println("" + entry.toString());
        for (String attribute : list_class) {
            //System.out.println(attribute);
            if (entry.toString().equals(attribute)) {
                System.out.println("isModefy: " + attribute);
                return 1;
            }
        }
        return 0;
    }

    public int readClassList(String list_file_name) {
        StringBuffer sb = new StringBuffer("");
        try {
            FileReader reader = new FileReader(list_file_name);
            BufferedReader br = new BufferedReader(reader);

            String str = null;

            while ((str = br.readLine()) != null) {
                //sb.append(str + "/n");
                list_class.add(str);
                System.out.println(str);
            }

            br.close();
            reader.close();
            return 0;
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
        return -1;
    }

}


