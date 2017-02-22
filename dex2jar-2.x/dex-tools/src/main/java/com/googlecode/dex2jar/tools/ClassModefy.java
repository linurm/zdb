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


import java.io.File;
import java.io.IOException;
import java.nio.file.FileSystem;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Enumeration;
import java.util.zip.ZipEntry;
import java.util.zip.ZipFile;


@BaseCmd.Syntax(cmd = "d2j-modefy-class", syntax = "[options] <dir>", desc = "Convert jar to dex by invoking dx.")
public class ClassModefy extends BaseCmd {
    @Opt(opt = "f", longOpt = "force", hasArg = false, description = "force overwrite")
    private boolean forceOverwrite = false;
    @Opt(opt = "o", longOpt = "output", description = "output .dex file, default is $current_dir/[jar-name]-jar2dex.dex", argName = "out-dex-file")
    private Path output;
    @Opt(opt = "c", longOpt = "class", description = "class name, default is $current_dir/[jar-name]-jar2dex.dex", argName = "class-file")
    private String clz;

    public static void main(String... args) {
        new ClassModefy().doMain(args);
    }

    @Override
    protected void doCommandLine() throws Exception {
        if (remainingArgs.length != 1) {
            usage();
            return;
        }

        Path jar = new File(remainingArgs[0]).toPath();
        //System.err.println("zj " + jar.toString());//zj ..\tmp\no1\Programmer.class
        if (!Files.exists(jar)) {
            System.err.println(jar + " is not exists");
            usage();
            return;
        }

        if (output == null) {
            if (Files.isDirectory(jar)) {
                output = new File(jar.getFileName() + "-jar2dex.dex").toPath();
            } else {
                output = new File(getBaseName(jar.getFileName().toString()) + "-jar2dex.dex").toPath();
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

            System.out.println("class modefy " + realJar + " -> " + output);
            String jars = realJar.toString();
            int index = jars.lastIndexOf(File.separator);


            String path = jars.substring(0, index + 1);
            System.err.println("path:" + path);
            File oldZipFile = new File(jars);

            ZipFile war = new ZipFile(oldZipFile.getAbsoluteFile());
            Enumeration<? extends ZipEntry> entries = war.entries();
            while (entries.hasMoreElements()) {
                ZipEntry e = entries.nextElement();
                if (e.toString().equals(clz)) {
                    System.err.println("" + e.toString());
                }System.err.println("" + e.toString());
            }
//            ClassReader classReader = new ClassReader(Files.readAllBytes(output));
//            ClassWriter classWriter = new ClassWriter(ClassWriter.COMPUTE_MAXS);
//            ClassAdapter classAdapter = new GeneralClassAdapter(classWriter);
//            classReader.accept(classAdapter, ClassReader.SKIP_DEBUG);
//            byte[] classFile = classWriter.toByteArray();
//            File file = new File(output.toString());
//            FileOutputStream fos = new FileOutputStream(file);
//            fos.write(classFile);

//            Class<?> c = Class.forName("com.android.dx.command.Main");
//            Method m = c.getMethod("main", String[].class);
//
//            List<String> ps = new ArrayList<String>();
//            ps.addAll(Arrays.asList("--dex", "--no-strict", "--output=" + output.toAbsolutePath().toString(), realJar
//                    .toAbsolutePath().toString()));
//            System.out.println("call com.android.dx.command.Main.main" + ps);
//            m.invoke(null, new Object[] { ps.toArray(new String[ps.size()]) });
        } finally {
            if (tmp != null) {
                Files.deleteIfExists(tmp);
            }
        }

    }
}
