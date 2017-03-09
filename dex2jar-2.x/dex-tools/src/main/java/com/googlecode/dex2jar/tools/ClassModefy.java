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

import static org.objectweb.asm.Opcodes.GETSTATIC;
import static org.objectweb.asm.Opcodes.INVOKEVIRTUAL;


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
            String pkg_class = clz.replace(".", "/") + ".class";
            while (entries.hasMoreElements()) {
                ZipEntry e = entries.nextElement();
                if (e.toString().equals(pkg_class)) {
                    System.err.println("" + e.toString());
                    ClassReader cr = new ClassReader(war.getInputStream(e));
                    ClassWriter cw = new ClassWriter(cr, ClassWriter.COMPUTE_MAXS);
                    ClassVisitor cv = new ClassVisitor(Opcodes.ASM4, cw) {
                        @Override
                        public void visit(int version, int access, String name, String signature, String superName, String[] interfaces) {
                            super.visit(version, access, name, signature, superName, interfaces);
                            //System.err.println("visit:" + access + " name: " + name + " : " + signature + " version: " + version);
                            //visit:33 name: com/example/Programmer : null version: 51
                        }

                        @Override
                        public MethodVisitor visitMethod(int access, String name, String desc, String signature,
                                                         String[] exceptions) {
                            System.err.println("visitMethod access:" + access + " name:" + name + " desc:" + desc + " signature:" + signature);
                            //visitMethod access:1 name:<init> desc:()V signature:null
                            //visitMethod access:2 name:code desc:(Ljava/lang/String;)Ljava/lang/String; signature:null
                            //visitMethod access:1 name:code desc:()V signature:null
                            //if(name.equals())
                            MethodVisitor mv = super.visitMethod(access, name, desc, signature, exceptions);
                            if(name.equals("<init>"))
                                return mv;

                            MethodVisitor newMethod = null;
                            newMethod = new AsmMethodVisit(mv); //访问需要修改的方法
                            return newMethod;
                            //return mv;
                        }

                        @Override
                        public FieldVisitor visitField(int access, String name, String desc, String signature, Object value) {
                            //visitField access:1 name:aBoolean desc:Z signature:null
                            //System.err.println("visitField access:" + access + " name:" + name + " desc:" + desc + " signature:" + signature);
                            return super.visitField(access, name, desc, signature, value);
                        }

                        @Override
                        public void visitEnd() {
                            super.visitEnd();

                            //System.err.println("visitEnd");
                        }
                    };
                    cr.accept(cv, Opcodes.ASM4);
                    byte[] code = cw.toByteArray();
                    FileOutputStream fos = new FileOutputStream(output.toString());
                    fos.write(code);
                    fos.close();
                    //zos.write(cw.toByteArray());
                }
                //System.err.println("" + e.toString());
            }

            ///////////////////////////////////////////////////////////////////////////////

        } finally {
            if (tmp != null) {
                Files.deleteIfExists(tmp);
            }
        }

    }

    static class AsmMethodVisit extends MethodVisitor {

        public AsmMethodVisit(MethodVisitor mv) {
            super(Opcodes.ASM4, mv);
        }

        @Override
        public void visitMethodInsn(int opcode, String owner, String name, String desc) {
            super.visitMethodInsn(opcode, owner, name, desc);
        }

        @Override
        public void visitCode() {
            //此方法在访问方法的头部时被访问到，仅被访问一次
            //此处可插入新的指令
            mv.visitFieldInsn(GETSTATIC,
                    "java/lang/System",
                    "out",
                    "Ljava/io/PrintStream;");
            // pushes the "Hello World!" String constant
            mv.visitLdcInsn("this is a modify method!");
            // invokes the 'println' method (defined in the PrintStream class)
            mv.visitMethodInsn(INVOKEVIRTUAL,
                    "java/io/PrintStream",
                    "println",
                    "(Ljava/lang/String;)V");

            super.visitCode();
        }

        @Override
        public void visitInsn(int opcode) {
            //此方法可以获取方法中每一条指令的操作类型，被访问多次
            //如应在方法结尾处添加新指令，则应判断：
            System.err.println("" + opcode);

            if (opcode == Opcodes.RETURN) {
                // pushes the 'out' field (of type PrintStream) of the System class

//                mv.visitInsn(RETURN);
            }
            super.visitInsn(opcode);
        }
    }

}
