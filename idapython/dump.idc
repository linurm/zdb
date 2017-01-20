auto fp, begin, end, dexbyte;  
fp = fopen("D:\\jiagu.so", "wb");  
begin = 0x76698000;  
end = begin + 0x6b90c;  
for ( dexbyte = begin; dexbyte < end; dexbyte ++ )  
    fputc(Byte(dexbyte), fp); 