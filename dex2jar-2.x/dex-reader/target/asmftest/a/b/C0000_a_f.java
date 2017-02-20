package a.b;
import com.googlecode.d2j.*;
import com.googlecode.d2j.visitors.*;
import static com.googlecode.d2j.DexConstants.*;
import static com.googlecode.d2j.reader.Op.*;
public class C0000_a_f {
    public static void accept(DexFileVisitor v) {
        DexClassVisitor cv=v.visit(ACC_PUBLIC,"La/f;","Ljava/lang/Object;",null);
        if(cv!=null) {
            accept(cv);
            cv.visitEnd();
        }
    }
    public static void accept(DexClassVisitor cv) {
        f000_abc(cv);
        m000_zz(cv);
    }
    public static void f000_abc(DexClassVisitor cv) {
        DexFieldVisitor fv=cv.visitField(ACC_PUBLIC, new Field("La/f;","abc","I"), null);
        if(fv != null) {
            fv.visitEnd();
        }
    }
    public static void m000_zz(DexClassVisitor cv) {
        DexMethodVisitor mv=cv.visitMethod(ACC_PUBLIC|ACC_STATIC, new Method("La/f;","zz",new String[]{ },"I"));
        if(mv != null) {
            DexAnnotationAble pv02 = mv.visitParameterAnnotation(2);
            if(pv02!=null){
                DexAnnotationVisitor av00 = pv02.visitAnnotation("Leeeff;", Visibility.BUILD);
                if(av00 != null) {
                    av00.visitEnd();
                }
            }
            DexCodeVisitor code=mv.visitCode();
            if(code != null) {
                code.visitConstStmt(FILL_ARRAY_DATA,0,new int[]{ 1,2,3});
                code.visitStmt0R(RETURN_VOID);
                code.visitEnd();
            }
            mv.visitEnd();
        }
    }
}
