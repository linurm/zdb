package com.googlecode.dex2jar.tools.ZjUtils;

import org.objectweb.asm.Label;
import org.objectweb.asm.MethodVisitor;
import org.objectweb.asm.Opcodes;
import org.objectweb.asm.ClassVisitor;

import static org.objectweb.asm.Opcodes.ALOAD;
import static org.objectweb.asm.Opcodes.ASTORE;
import static org.objectweb.asm.Opcodes.GETSTATIC;
import static org.objectweb.asm.Opcodes.RETURN;
import static org.objectweb.asm.Opcodes.*;

/**
 * Created by Administrator on 2017/3/10.
 */

public class GenMethodAndFunc {
    public static void everyMethodAddCode2(MethodVisitor mv) {
        mv.visitFieldInsn(GETSTATIC, "java/lang/System", "out", "Ljava/io/PrintStream;");
        mv.visitLdcInsn("add by zj");
        mv.visitMethodInsn(Opcodes.INVOKEVIRTUAL, "java/io/PrintStream", "println", "(Ljava/lang/String;)V");
    }

    public static void theMethodAddCode(MethodVisitor mv) {
        Label l0 = new Label();
        mv.visitLabel(l0);
        mv.visitLineNumber(6, l0);
        mv.visitMethodInsn(INVOKESTATIC, "com/googlecode/dex2jar/tools/ZjUtils/Utils", "printStack", "()V", false);
    }

    public static void classAddMethod(ClassVisitor cw) {

        MethodVisitor mv = cw.visitMethod(ACC_PUBLIC + ACC_STATIC, "printStack", "()V", null, null);
        mv.visitCode();
        Label l0 = new Label();
        mv.visitLabel(l0);
        mv.visitLineNumber(7, l0);
        mv.visitTypeInsn(NEW, "java/lang/Throwable");
        mv.visitInsn(DUP);
        mv.visitMethodInsn(INVOKESPECIAL, "java/lang/Throwable", "<init>", "()V", false);
        mv.visitVarInsn(ASTORE, 0);
        Label l1 = new Label();
        mv.visitLabel(l1);
        mv.visitLineNumber(8, l1);
        mv.visitVarInsn(ALOAD, 0);
        mv.visitMethodInsn(INVOKEVIRTUAL, "java/lang/Throwable", "getStackTrace", "()[Ljava/lang/StackTraceElement;", false);
        mv.visitVarInsn(ASTORE, 1);
        Label l2 = new Label();
        mv.visitLabel(l2);
        mv.visitLineNumber(9, l2);
        mv.visitVarInsn(ALOAD, 1);
        Label l3 = new Label();
        mv.visitJumpInsn(IFNULL, l3);
        Label l4 = new Label();
        mv.visitLabel(l4);
        mv.visitLineNumber(10, l4);
        mv.visitInsn(ICONST_0);
        mv.visitVarInsn(ISTORE, 2);
        Label l5 = new Label();
        mv.visitLabel(l5);
        Label l6 = new Label();
        mv.visitJumpInsn(GOTO, l6);
        Label l7 = new Label();
        mv.visitLabel(l7);
        mv.visitLineNumber(11, l7);
        mv.visitFrame(Opcodes.F_APPEND,3, new Object[] {"java/lang/Throwable", "[Ljava/lang/StackTraceElement;", Opcodes.INTEGER}, 0, null);
        mv.visitFieldInsn(GETSTATIC, "java/lang/System", "out", "Ljava/io/PrintStream;");
        mv.visitTypeInsn(NEW, "java/lang/StringBuilder");
        mv.visitInsn(DUP);
        mv.visitVarInsn(ALOAD, 1);
        mv.visitVarInsn(ILOAD, 2);
        mv.visitInsn(AALOAD);
        mv.visitMethodInsn(INVOKEVIRTUAL, "java/lang/StackTraceElement", "getClassName", "()Ljava/lang/String;", false);
        mv.visitMethodInsn(INVOKESTATIC, "java/lang/String", "valueOf", "(Ljava/lang/Object;)Ljava/lang/String;", false);
        mv.visitMethodInsn(INVOKESPECIAL, "java/lang/StringBuilder", "<init>", "(Ljava/lang/String;)V", false);
        mv.visitLdcInsn("/t");
        mv.visitMethodInsn(INVOKEVIRTUAL, "java/lang/StringBuilder", "append", "(Ljava/lang/String;)Ljava/lang/StringBuilder;", false);
        mv.visitMethodInsn(INVOKEVIRTUAL, "java/lang/StringBuilder", "toString", "()Ljava/lang/String;", false);
        mv.visitMethodInsn(INVOKEVIRTUAL, "java/io/PrintStream", "print", "(Ljava/lang/String;)V", false);
        Label l8 = new Label();
        mv.visitLabel(l8);
        mv.visitLineNumber(12, l8);
        mv.visitFieldInsn(GETSTATIC, "java/lang/System", "out", "Ljava/io/PrintStream;");
        mv.visitTypeInsn(NEW, "java/lang/StringBuilder");
        mv.visitInsn(DUP);
        mv.visitVarInsn(ALOAD, 1);
        mv.visitVarInsn(ILOAD, 2);
        mv.visitInsn(AALOAD);
        mv.visitMethodInsn(INVOKEVIRTUAL, "java/lang/StackTraceElement", "getFileName", "()Ljava/lang/String;", false);
        mv.visitMethodInsn(INVOKESTATIC, "java/lang/String", "valueOf", "(Ljava/lang/Object;)Ljava/lang/String;", false);
        mv.visitMethodInsn(INVOKESPECIAL, "java/lang/StringBuilder", "<init>", "(Ljava/lang/String;)V", false);
        mv.visitLdcInsn("/t");
        mv.visitMethodInsn(INVOKEVIRTUAL, "java/lang/StringBuilder", "append", "(Ljava/lang/String;)Ljava/lang/StringBuilder;", false);
        mv.visitMethodInsn(INVOKEVIRTUAL, "java/lang/StringBuilder", "toString", "()Ljava/lang/String;", false);
        mv.visitMethodInsn(INVOKEVIRTUAL, "java/io/PrintStream", "print", "(Ljava/lang/String;)V", false);
        Label l9 = new Label();
        mv.visitLabel(l9);
        mv.visitLineNumber(13, l9);
        mv.visitFieldInsn(GETSTATIC, "java/lang/System", "out", "Ljava/io/PrintStream;");
        mv.visitTypeInsn(NEW, "java/lang/StringBuilder");
        mv.visitInsn(DUP);
        mv.visitVarInsn(ALOAD, 1);
        mv.visitVarInsn(ILOAD, 2);
        mv.visitInsn(AALOAD);
        mv.visitMethodInsn(INVOKEVIRTUAL, "java/lang/StackTraceElement", "getLineNumber", "()I", false);
        mv.visitMethodInsn(INVOKESTATIC, "java/lang/String", "valueOf", "(I)Ljava/lang/String;", false);
        mv.visitMethodInsn(INVOKESPECIAL, "java/lang/StringBuilder", "<init>", "(Ljava/lang/String;)V", false);
        mv.visitLdcInsn("/t");
        mv.visitMethodInsn(INVOKEVIRTUAL, "java/lang/StringBuilder", "append", "(Ljava/lang/String;)Ljava/lang/StringBuilder;", false);
        mv.visitMethodInsn(INVOKEVIRTUAL, "java/lang/StringBuilder", "toString", "()Ljava/lang/String;", false);
        mv.visitMethodInsn(INVOKEVIRTUAL, "java/io/PrintStream", "print", "(Ljava/lang/String;)V", false);
        Label l10 = new Label();
        mv.visitLabel(l10);
        mv.visitLineNumber(14, l10);
        mv.visitFieldInsn(GETSTATIC, "java/lang/System", "out", "Ljava/io/PrintStream;");
        mv.visitVarInsn(ALOAD, 1);
        mv.visitVarInsn(ILOAD, 2);
        mv.visitInsn(AALOAD);
        mv.visitMethodInsn(INVOKEVIRTUAL, "java/lang/StackTraceElement", "getMethodName", "()Ljava/lang/String;", false);
        mv.visitMethodInsn(INVOKEVIRTUAL, "java/io/PrintStream", "println", "(Ljava/lang/String;)V", false);
        Label l11 = new Label();
        mv.visitLabel(l11);
        mv.visitLineNumber(15, l11);
        mv.visitFieldInsn(GETSTATIC, "java/lang/System", "out", "Ljava/io/PrintStream;");
        mv.visitLdcInsn("-----------------------------------");
        mv.visitMethodInsn(INVOKEVIRTUAL, "java/io/PrintStream", "println", "(Ljava/lang/String;)V", false);
        Label l12 = new Label();
        mv.visitLabel(l12);
        mv.visitLineNumber(10, l12);
        mv.visitIincInsn(2, 1);
        mv.visitLabel(l6);
        mv.visitFrame(Opcodes.F_SAME, 0, null, 0, null);
        mv.visitVarInsn(ILOAD, 2);
        mv.visitVarInsn(ALOAD, 1);
        mv.visitInsn(ARRAYLENGTH);
        mv.visitJumpInsn(IF_ICMPLT, l7);
        mv.visitLabel(l3);
        mv.visitLineNumber(18, l3);
        mv.visitFrame(Opcodes.F_CHOP,1, null, 0, null);
        mv.visitInsn(RETURN);
        Label l13 = new Label();
        mv.visitLabel(l13);
        mv.visitLocalVariable("ex", "Ljava/lang/Throwable;", null, l1, l13, 0);
        mv.visitLocalVariable("stackElements", "[Ljava/lang/StackTraceElement;", null, l2, l13, 1);
        mv.visitLocalVariable("i", "I", null, l5, l3, 2);
        mv.visitMaxs(5, 3);
        mv.visitEnd();

    }
}
