package com.googlecode.dex2jar.tools.ZjUtils;

public class Utils {
	
	
	public static void printStack(){
        Throwable ex = new Throwable();
        StackTraceElement[] stackElements = ex.getStackTrace();
        if (stackElements != null) {
            for (int i = 0; i < stackElements.length; i++) {
                System.out.print(stackElements[i].getClassName()+"@");
                System.out.print(stackElements[i].getFileName()+":");
                System.out.print(stackElements[i].getLineNumber()+":");
                System.out.println(stackElements[i].getMethodName());
                System.out.println("-----------------------------------");
            }
        }
    }

}
