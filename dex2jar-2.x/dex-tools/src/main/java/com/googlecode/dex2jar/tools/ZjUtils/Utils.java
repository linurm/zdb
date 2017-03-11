package com.googlecode.dex2jar.tools.ZjUtils;

import org.objectweb.asm.Label;
import org.objectweb.asm.MethodVisitor;
import org.objectweb.asm.Opcodes;
import org.objectweb.asm.ClassVisitor;

import static com.android.dx.cf.code.ByteOps.INVOKEVIRTUAL;
import static org.objectweb.asm.Opcodes.ALOAD;
import static org.objectweb.asm.Opcodes.ASTORE;
import static org.objectweb.asm.Opcodes.GETSTATIC;
import static org.objectweb.asm.Opcodes.RETURN;

/**
 * Created by Administrator on 2017/3/10.
 */

public class Utils {
    public static void everyMethodAddCode2(MethodVisitor mv) {
        mv.visitFieldInsn(GETSTATIC, "java/lang/System", "out", "Ljava/io/PrintStream;");
        mv.visitLdcInsn("add by zj");
        mv.visitMethodInsn(Opcodes.INVOKEVIRTUAL, "java/io/PrintStream", "println", "(Ljava/lang/String;)V");
    }
    public static void theMethodAddCode(MethodVisitor mv) {
        //MethodVisitor mv = cw.visitMethod(Opcodes.ACC_PUBLIC + Opcodes.ACC_STATIC, "fun2", "()V", null, null);
        Label l0 = new Label();
        mv.visitLabel(l0);
        mv.visitLineNumber(6, l0);
        mv.visitLdcInsn("add by zj");
        mv.visitVarInsn(ASTORE, 0);
        Label l1 = new Label();
        mv.visitLabel(l1);
        mv.visitLineNumber(7, l1);
        mv.visitFieldInsn(GETSTATIC, "java/lang/System", "out", "Ljava/io/PrintStream;");
        mv.visitVarInsn(ALOAD, 0);
        mv.visitMethodInsn(INVOKEVIRTUAL, "java/io/PrintStream", "println", "(Ljava/lang/String;)V", false);
//        Label l2 = new Label();
//        mv.visitLabel(l2);
//        mv.visitLineNumber(8, l2);
//        mv.visitInsn(RETURN);
        Label l3 = new Label();
        mv.visitLabel(l3);
        mv.visitLocalVariable("sss", "Ljava/lang/String;", null, l1, l3, 0);
        mv.visitMaxs(2, 1);
    }
    public static void classAddMethod(ClassVisitor cw){
        MethodVisitor mv = cw.visitMethod(Opcodes.ACC_PUBLIC + Opcodes.ACC_STATIC, "fun2", "()V", null, null);
        mv.visitCode();
        Label l0 = new Label();
        mv.visitLabel(l0);
        mv.visitLineNumber(20, l0);
        mv.visitMethodInsn(Opcodes.INVOKESTATIC, "java/lang/Thread", "currentThread", "()Ljava/lang/Thread;", false);
        mv.visitMethodInsn(Opcodes.INVOKEVIRTUAL, "java/lang/Thread", "getStackTrace", "()[Ljava/lang/StackTraceElement;", false);
        mv.visitInsn(Opcodes.ICONST_1);
        mv.visitInsn(Opcodes.AALOAD);
        mv.visitMethodInsn(Opcodes.INVOKEVIRTUAL, "java/lang/StackTraceElement", "getMethodName", "()Ljava/lang/String;", false);
        mv.visitVarInsn(ASTORE, 0);
        Label l1 = new Label();
        mv.visitLabel(l1);
        mv.visitLineNumber(21, l1);
        mv.visitMethodInsn(Opcodes.INVOKESTATIC, "java/lang/Thread", "currentThread", "()Ljava/lang/Thread;", false);
        mv.visitMethodInsn(Opcodes.INVOKEVIRTUAL, "java/lang/Thread", "getStackTrace", "()[Ljava/lang/StackTraceElement;", false);
        mv.visitInsn(Opcodes.ICONST_1);
        mv.visitInsn(Opcodes.AALOAD);
        Label l2 = new Label();
        mv.visitLabel(l2);
        mv.visitLineNumber(22, l2);
        mv.visitMethodInsn(Opcodes.INVOKEVIRTUAL, "java/lang/StackTraceElement", "getLineNumber", "()I", false);
        Label l3 = new Label();
        mv.visitLabel(l3);
        mv.visitLineNumber(21, l3);
        mv.visitVarInsn(Opcodes.ISTORE, 1);
        Label l4 = new Label();
        mv.visitLabel(l4);
        mv.visitLineNumber(23, l4);
        mv.visitFieldInsn(GETSTATIC, "java/lang/System", "out", "Ljava/io/PrintStream;");
        mv.visitTypeInsn(Opcodes.NEW, "java/lang/StringBuilder");
        mv.visitInsn(Opcodes.DUP);
        mv.visitVarInsn(ALOAD, 0);
        mv.visitMethodInsn(Opcodes.INVOKESTATIC, "java/lang/String", "valueOf", "(Ljava/lang/Object;)Ljava/lang/String;", false);
        mv.visitMethodInsn(Opcodes.INVOKESPECIAL, "java/lang/StringBuilder", "<init>", "(Ljava/lang/String;)V", false);
        mv.visitLdcInsn(":");
        mv.visitMethodInsn(Opcodes.INVOKEVIRTUAL, "java/lang/StringBuilder", "append", "(Ljava/lang/String;)Ljava/lang/StringBuilder;", false);
        mv.visitVarInsn(Opcodes.ILOAD, 1);
        mv.visitMethodInsn(Opcodes.INVOKEVIRTUAL, "java/lang/StringBuilder", "append", "(I)Ljava/lang/StringBuilder;", false);
        mv.visitMethodInsn(Opcodes.INVOKEVIRTUAL, "java/lang/StringBuilder", "toString", "()Ljava/lang/String;", false);
        mv.visitMethodInsn(Opcodes.INVOKEVIRTUAL, "java/io/PrintStream", "println", "(Ljava/lang/String;)V", false);
        Label l5 = new Label();
        mv.visitLabel(l5);
        mv.visitLineNumber(24, l5);
        mv.visitInsn(RETURN);
        Label l6 = new Label();
        mv.visitLabel(l6);
        mv.visitLocalVariable("name", "Ljava/lang/String;", null, l1, l6, 0);
        mv.visitLocalVariable("line_num", "I", null, l4, l6, 1);
        mv.visitMaxs(4, 2);
        mv.visitEnd();
    }
}
