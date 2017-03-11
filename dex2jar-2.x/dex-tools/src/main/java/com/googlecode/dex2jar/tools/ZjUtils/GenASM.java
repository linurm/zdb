package com.googlecode.dex2jar.tools.ZjUtils;

/**
 * Created by Administrator on 2017/3/10.
 */

public class GenASM {
    //print current class name
    static public void fun1() {
        String clazzName3 = new Object() {
            public String getClassName() {
                String clazzName = this.getClass().getName();
                return clazzName.substring(0, clazzName.lastIndexOf('$'));
            }
        }.getClassName();
        System.out.println(clazzName3);
    }
}
