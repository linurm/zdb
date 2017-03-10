package com.googlecode.dex2jar.tools.ZjUtils;

import org.objectweb.asm.Label;
import org.objectweb.asm.MethodVisitor;
import org.objectweb.asm.Opcodes;

import static org.objectweb.asm.Opcodes.ACC_PUBLIC;
import static org.objectweb.asm.Opcodes.ALOAD;
import static org.objectweb.asm.Opcodes.ASTORE;
import static org.objectweb.asm.Opcodes.DUP;
import static org.objectweb.asm.Opcodes.GETSTATIC;
import static org.objectweb.asm.Opcodes.INVOKESPECIAL;
import static org.objectweb.asm.Opcodes.INVOKEVIRTUAL;
import static org.objectweb.asm.Opcodes.NEW;
import static org.objectweb.asm.Opcodes.RETURN;

/**
 * Created by Administrator on 2017/3/10.
 */

public class Utils {
    public static void everyMethodAddCode(MethodVisitor mv) {
        mv.visitFieldInsn(GETSTATIC, "java/lang/System", "out", "Ljava/io/PrintStream;");
        mv.visitLdcInsn("add by zj");
        mv.visitMethodInsn(INVOKEVIRTUAL, "java/io/PrintStream", "println", "(Ljava/lang/String;)V");
    }
    /*public static void everyMethodAddCode(MethodVisitor mv){
        mv = cw.visitMethod(ACC_PUBLIC, "fun1", "()V", null, null);
        mv.visitCode();
        Label l0 = new Label();
        mv.visitLabel(l0);
        mv.visitLineNumber(10, l0);
        mv.visitTypeInsn(NEW, "com/googlecode/dex2jar/tools/ZjUtils/GenASM$1");
        mv.visitInsn(DUP);
        mv.visitVarInsn(ALOAD, 0);
        mv.visitMethodInsn(INVOKESPECIAL, "com/googlecode/dex2jar/tools/ZjUtils/GenASM$1", "<init>", "(Lcom/googlecode/dex2jar/tools/ZjUtils/GenASM;)V", false);
        Label l1 = new Label();
        mv.visitLabel(l1);
        mv.visitLineNumber(15, l1);
        mv.visitMethodInsn(INVOKEVIRTUAL, "com/googlecode/dex2jar/tools/ZjUtils/GenASM$1", "getClassName", "()Ljava/lang/String;", false);
        mv.visitVarInsn(ASTORE, 1);
        Label l2 = new Label();
        mv.visitLabel(l2);
        mv.visitLineNumber(16, l2);
        mv.visitFieldInsn(GETSTATIC, "java/lang/System", "out", "Ljava/io/PrintStream;");
        mv.visitVarInsn(ALOAD, 1);
        mv.visitMethodInsn(INVOKEVIRTUAL, "java/io/PrintStream", "println", "(Ljava/lang/String;)V", false);
        Label l3 = new Label();
        mv.visitLabel(l3);
        mv.visitLineNumber(17, l3);
        mv.visitInsn(RETURN);
        Label l4 = new Label();
        mv.visitLabel(l4);
        mv.visitLocalVariable("this", "Lcom/googlecode/dex2jar/tools/ZjUtils/GenASM;", null, l0, l4, 0);
        mv.visitLocalVariable("clazzName3", "Ljava/lang/String;", null, l2, l4, 1);
        mv.visitMaxs(3, 2);
        mv.visitEnd();
    }*/
}
