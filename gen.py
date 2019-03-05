import affineCipher, caesarCipher, transpositionEncrypt , transpositionDecrypt , vigenereCipher , affineKeyTest
import random
import hashlib

def md5():
        outputFilename = "hashmd5.out"                                                                           
        outputFileObj = open(outputFilename, 'w')
        for i in range(0,5000):
            num = ("0"*(4-len(str(i)))+str(i))
            outputFileObj.write(num+": "+hashlib.md5(num.encode('utf-8')).hexdigest()+"\n")
        outputFileObj.close()
                


def main():
    inp1 = ['Hola vamos donde el mono' , 'este viernes para comer' , 'unas ricas empanadas de doce mil' , 'y pasar un buen rato entre amigos' , 'e ir despues a  shaki shaki!']
    inp = [
               '4a7d1ed414474e4033ac29ccb8653d9b',
               '25bbdcd06c32d477f7fa1c3e4a91b032' ,
               '0e7e3cf0ded4d9db8b376b317c007f99' ,
               '7cd86ecb09aa48c6e620b340f6a74592',
               'bd2f40f24260bc41db48d82d5e7abf1d']
    outputFilename = "resultados.out"                                                                           
    outputFileObj = open(outputFilename, 'w')
    for text in inp:
        n  = random.randint(1,4)
        key, cadena = "",""
        if(n==1):
            key, cadena = affineKeyTest.prueba(text)
            translate = "Affine-" + str(key) + "-CipherText-" + str(cadena)
        elif(n==2):
            key, cadena = caesarCipher.Cipher(text)
            translate = "Caesar-" + str(key) + "-CipherText-" + str(cadena)
        elif(n==3):
            key = random.randint(1,66)
            cadena = transpositionEncrypt.encryptMessage(key,text)
            translate = "Transposition-" + str(key) + "-CipherText-" + str(cadena)
        elif(n==4):
            key2 = random.randint(1,66)
            key = transpositionEncrypt.encryptMessage(key2,text)
            print(key)
            cadena = vigenereCipher.encryptMessage('SPTI', text)
            translate = "vigenereCipher-" + str(key) + "-CipherText-" + str(cadena)
        key, cad = affineKeyTest.prueba(cadena)
        translate += "\nAffine-" + str(key) + "-CipherText-" + str(cad)
        outputFileObj.write(translate+"\n")
    outputFileObj.close()


    fileObj = open(outputFilename)
    content = fileObj.read()
    lec  = content.split('\n')
    lon = len(lec)-1
    print(content)
    print("_"*10)
    for i in range(0,lon,2):
        line1 = lec[i].split('-')
        line2 = lec[i+1].split('-')
        print(line2[1], line2[3] , end =" affineDecrypt ")      
        affineDecrypt = affineCipher.decryptMessage(int(line2[1]),line2[3])
        print(affineDecrypt , end = " ")
        if(line1[0]=='Affine'):
            cadena = affineCipher.decryptMessage(int(line1[1]), affineDecrypt)
            print('Affine ', cadena)
        if(line1[0]=='Caesar'):        
            cadena = caesarCipher.decryptMessage(int(line1[1]),affineDecrypt)
            print("Caesar",cadena)
        if(line1[0]=='Transposition'):        
            key = random.randint(1,66)
            cadena = transpositionDecrypt.decryptMessage(int(line1[1]),affineDecrypt)
            print("Transposition",cadena)
        if(line1[0]=='vigenereCipher'):        
            cadena = vigenereCipher.decryptMessage('SPTI', affineDecrypt)
            print("Transposition",cadena)
        print()                
    fileObj.close()

