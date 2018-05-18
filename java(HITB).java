import java.util.Arrays;

public class Check {
    public static void main(String[] args) {
        StringBuilder flag = new StringBuilder();
        for (int i = 0; i < 32; i += 8) {
            byte[] expectedInput = Check.decode8Bytes(f1b, i);
            flag.append(new String(expectedInput));
        }
        System.out.println(flag);
    }
    private static int[] f0a = new int[]{-1414812757, -842150451, -269488145, 305419896};
    private static byte[] f1b = new byte[]{(byte) 99, (byte) 124, (byte) 101, (byte) -23, (byte) -114, (byte) 81, (byte) -47, (byte) -39, (byte) -102, (byte) 79, (byte) 22, (byte) 52, (byte) -39, (byte) -94, (byte) -66, (byte) -72, (byte) 101, (byte) -18, (byte) 73, (byte) -27, (byte) 53, (byte) -5, (byte) 46, (byte) -20, (byte) 97, (byte) 11, (byte) -56, (byte) 36, (byte) -19, (byte) -49, (byte) -112, (byte) -75};
     
     static byte[] decode8Bytes(byte[] inputData,int startIndex){
        int[] a = Check.m4a(inputData,startIndex);  //byte to int
        int firstInt = a[0];
        int secondInt = a[1];
        int i5 = -1640531527*32;
        int i6 = f0a[0];
        int i7 = f0a[1];
        int i8 = f0a[2];
        int i9 = f0a[3];
        for(int i10 = 0; i10 < 32; i10++){
            secondInt -= (((firstInt << 4) + i8) ^ (firstInt + i5)) ^ ((firstInt >> 5) + i9);
            firstInt -= (((secondInt << 4) + i6) ^ (secondInt + i5)) ^ ((secondInt >> 5) + i7);
            i5 += 1640531527;
        }
        
        int[] result = new int[2];
        result[0] = firstInt;
        result[1] = secondInt;
        
        return Check.m3a(result,0); //int to byte
     }
     
    static byte[] m2a(byte[] bArr, int i, int[] iArr, int i2) {
        int[] a = Check.m4a(bArr, i);   //byte to int
        int i3 = a[0];
        int i4 = a[1];
        int i5 = 0;
        int i6 = iArr[0];
        int i7 = iArr[1];
        int i8 = iArr[2];
        int i9 = iArr[3];
        for (int i10 = 0; i10 < i2; i10++) {
            i5 -= 1640531527;
            i3 += (((i4 << 4) + i6) ^ (i4 + i5)) ^ ((i4 >> 5) + i7);
            i4 += (((i3 << 4) + i8) ^ (i3 + i5)) ^ ((i3 >> 5) + i9);
        }
        a[0] = i3;
        a[1] = i4;
        return Check.m3a(a, 0); // int to byte
    }

    private static int[] m4a(byte[] bArr, int i) {  //byte to int
        int[] iArr = new int[(bArr.length >> 2)];
        int i2 = 0;
        while (i < bArr.length) {
            iArr[i2] = ((Check.m0a(bArr[i + 3]) | (Check.m0a(bArr[i + 2]) << 8)) | (Check.m0a(bArr[i + 1]) << 16)) | (bArr[i] << 24);
            i2++;
            i += 4;
        }
        return iArr;
    }

    private static byte[] m3a(int[] iArr, int i) {  //int to byte
        byte[] bArr = new byte[(iArr.length << 2)];
        int i2 = 0;
        while (i < bArr.length) {
            bArr[i + 3] = (byte) (iArr[i2] & 255);
            bArr[i + 2] = (byte) ((iArr[i2] >> 8) & 255);
            bArr[i + 1] = (byte) ((iArr[i2] >> 16) & 255);
            bArr[i] = (byte) ((iArr[i2] >> 24) & 255);
            i2++;
            i += 4;
        }
        return bArr;
    }

    private static int m0a(byte b) {
        if (b < (byte) 0) {
            return b + 256;
        }
        return b;
    }

    public static byte[] m1a(byte[] bArr) {
        int length = 8 - (bArr.length % 8);
        byte obj[] = new byte[(bArr.length + length)];
        obj[0] = (byte) length;
        System.arraycopy(bArr, 0, obj, length, bArr.length);
        byte obj2[] = new byte[obj.length];
        for (length = 0; length < obj2.length; length += 8) {
            System.arraycopy(Check.m2a(obj, length, f0a, 32), 0, obj2, length, 8);
        }
        return obj;
    }

    public static byte[] check(String str) {
        return str.getBytes();
    }
}
