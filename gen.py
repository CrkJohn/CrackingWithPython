import affineCipher, caesarCipher, transpositionEncrypt , transpositionDecrypt , vigenereCipher , affineKeyTest
import random
import hashlib

def md5Gen():
        outputFilename = "hashmd5.out"                                                                           
        outputFileObj = open(outputFilename, 'w')
        for i in range(0,5000):
            num = ("0"*(4-len(str(i)))+str(i))
            outputFileObj.write(num+": "+hashlib.md5(num.encode('utf-8')).hexdigest()+"\n")
        outputFileObj.close()

def md5(i):
        num = ("0"*(4-len(str(i)))+str(i))
        
        return (str(num),hashlib.md5(num.encode('utf-8')).hexdigest())


def main():
    inp1 = ['Hola vamos donde el mono' , 'este viernes para comer' , 'unas ricas empanadas de doce mil' , 'y pasar un buen rato entre amigos' , 'e ir despues a  shaki shaki!']
    Primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167,
              173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359,
              367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571,
              577, 587, 593, 599, 601, 607, 613, 617,619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787,
              797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941]
    inp = [    '4a7d1ed414474e4033ac29ccb8653d9b',
               '25bbdcd06c32d477f7fa1c3e4a91b032' ,
               '0e7e3cf0ded4d9db8b376b317c007f99' ,
               '7cd86ecb09aa48c6e620b340f6a74592',
               'bd2f40f24260bc41db48d82d5e7abf1d']
    outputFilename = "resultados.out"                                                                           
    outputFileObj = open(outputFilename, 'w')

    outputFile = "llaves.out"                                                                           
    outpu= open(outputFile, 'w')
    for group in range(10):
        outputFileObj.write("Equipo numero {}\n \t".format(group+1))
        numberPerm = list()
        outpu.write("Equipo numero {}\n \t".format(group+1))
        print("Equipo numero {}\n \t".format(group+1))
        for numberKey in range(3):                
                randomInt = random.choice(Primes)
                NumAndmd5Text = md5(randomInt)
                num = NumAndmd5Text[0]
                if(numberKey<=2):
                        numberPerm.append(randomInt)
                text = NumAndmd5Text[1]
                n  = random.randint(1,4)
                outputFileObj.write('\n'+str(num) +":"+ str(text) + "\n \t")
                key, cadena = "",""
                if(n==1):
                    key, cadena = affineKeyTest.prueba(text)
                    translate = "AffineClave:" + str(key) + "-CipherText-" + str(cadena)+"-"
                elif(n==2):
                    key, cadena = caesarCipher.Cipher(text)
                    translate = "CaesarClave:" + str(key) + "-CipherText-" + str(cadena)+"-"
                elif(n==3):
                    key = random.randint(1,66)
                    cadena = transpositionEncrypt.encryptMessage(key,text)
                    translate = "TranspositionClave:" + str(key) + "-CipherText-" + str(cadena)+"-"
                elif(n==4):
                    key2 = random.randint(1,66)
                    key = 'SPTI'
                    cadena = vigenereCipher.encryptMessage('SPTI', text)
                    translate = "vigenereCipherClave:SPTI-CipherText-" + str(cadena)+"-"
                tmpKey = key  
                key, cad = affineKeyTest.prueba(cadena)
                translate += "\n \t \t Affine-" + str(key) + "-CipherText-" + str(cad)+"-"
                endChar = "\n \t" if(numberKey != 4) else   "\n"
                exi = "\t el {} archivo las siguientes : \n \t  para la primera descriptacion la llave es {} y la para el segundo la llave es  {}".format(numberKey+1,key,tmpKey)
                outpu.write(exi)
                print(exi)
                outputFileObj.write(translate+endChar)

        numberPermMultiplicacion = list()
        for i in range(3):
                for j in range(i+1,3):
                        numberPermMultiplicacion.append(numberPerm[i]*numberPerm[j])                        
        outputFileObj.write("\n \t Yowis ")
        for npm in numberPerm:
                outputFileObj.write(str(npm)+" ")
        outputFileObj.write(" numberPermMultiplicacion ")
        for npm in numberPermMultiplicacion:
                outputFileObj.write(str(npm)+":"+str(md5(npm)[1])+"\n \t \t \t \t \t \t\t \t \t \t \t \t ")

        outputFileObj.write("\n")
        

                                    
    outputFileObj.close()
    outpu.close()
    """
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
    """

main()
