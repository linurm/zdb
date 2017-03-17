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
package com.googlecode.dex2jar.tools;


import com.googlecode.dex2jar.tools.ZjUtils.GenMethodAndFunc;

import org.objectweb.asm.ClassReader;
import org.objectweb.asm.ClassVisitor;
import org.objectweb.asm.ClassWriter;
import org.objectweb.asm.FieldVisitor;
import org.objectweb.asm.MethodVisitor;
import org.objectweb.asm.Opcodes;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.nio.file.FileSystem;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Enumeration;
import java.util.zip.ZipEntry;
import java.util.zip.ZipFile;


@BaseCmd.Syntax(cmd = "d2j-list-all-class", syntax = "[options] <dir>", desc = "list all class of the apk(jar)")

public class ListAllClass extends BaseCmd {
    @Opt(opt = "f", longOpt = "force", hasArg = false, description = "force overwrite")
    private boolean forceOverwrite = false;
    @Opt(opt = "o", longOpt = "output", description = "output .dex file, default is $current_dir/[jar-name]-jar2dex.dex", argName = "out-dex-file")
    private Path output;
    @Opt(opt = "c", longOpt = "class", description = "class name, default is $current_dir/[jar-name]-jar2dex.dex", argName = "class-file")
    private String clz;
    @Opt(opt = "d", longOpt = "debug", hasArg = false, description = "debug", argName = "debug")
    private boolean debug = false;

    public static void main(String... args) {
        new ListAllClass().doMain(args);
    }

    @Override
    protected void doCommandLine() throws Exception {
        if (remainingArgs.length != 1) {
            usage();
            return;
        }

        Path jar = new File(remainingArgs[0]).toPath();
        System.err.println("zj " + jar.toString());//zj ..\tmp\no1\Programmer.class
        if (!Files.exists(jar)) {
            System.err.println(jar + " is not exists");
            usage();
            return;
        }

        if (output == null) {
            if (Files.isDirectory(jar)) {
                output = new File(jar.getFileName() + "-jar2dex.dex").toPath();
            } else {
                output = new File(jar.getFileName().toString() + "-jar2dex.dex").toPath();
            }
        }

        if (Files.exists(output) && !forceOverwrite) {
            System.err.println(output + " exists, use --force to overwrite");
            usage();
            return;
        }

        Path tmp = null;
        final Path realJar;
        try {
            if (Files.isDirectory(jar)) {
                realJar = Files.createTempFile("d2j", ".jar");
                tmp = realJar;
                System.out.println("zipping " + jar + " -> " + realJar);
                try (FileSystem fs = createZip(realJar)) {
                    final Path outRoot = fs.getPath("/");
                    walkJarOrDir(jar, new FileVisitorX() {
                        @Override
                        public void visitFile(Path file, String relative) throws IOException {
                            if (file.getFileName().toString().endsWith(".class")) {
                                Files.copy(file, outRoot.resolve(relative));
                            }
                        }
                    });
                }
            } else {
                realJar = jar;
            }


            String jars = realJar.toString();
            int index = jars.lastIndexOf(File.separator);


            String path = jars.substring(0, index + 1);
            FileOutputStream fos = new FileOutputStream(output.toString());
            File oldZipFile = new File(jars);
            System.err.println("path:" + oldZipFile.getAbsoluteFile());
            ZipFile war = new ZipFile(oldZipFile.getAbsoluteFile());
            Enumeration<? extends ZipEntry> entries = war.entries();
//            String pkg_class = clz.replace(".", "/") + ".class";
            System.out.println("class list " + realJar + " -> " + output);
            String entryStr = null;
            while (entries.hasMoreElements()) {
                ZipEntry e = entries.nextElement();
//                if (e.toString().equals(pkg_class)) {
                entryStr = e.toString();
                if (entryStr.endsWith(".class")) {
                    if (entryStr.contains("R.") || entryStr.contains("$") || entryStr.startsWith("android/support") || entryStr.startsWith("org/apache")) {
                        continue;
                    }
                    System.err.println("" + e.toString());
                    fos.write(e.toString().getBytes());
                    fos.write('\n');
                }


//                    FileOutputStream fos = new FileOutputStream(output.toString());
//                    fos.write(code);
//                    fos.close();

                //zos.write(cw.toByteArray());
//                }
                //System.err.println("" + e.toString());
            }
            fos.close();
        } finally {
            if (tmp != null) {
                Files.deleteIfExists(tmp);
            }
        }
    }
}
