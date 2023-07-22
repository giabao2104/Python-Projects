import matplotlib.pyplot as plt #Importing functions
import numpy as np
import scipy.ndimage as ndimage
    
#PART 1
###############################################################################

def getUserImage(): #Function asks user for image
    img = input("What is the name of the image? Include file type .jpg, .png, or .tiff: ") #Input image name
    image = plt.imread(img)
    if ".png" in img: #If file types are .png or .tiff the data type must be converted/adjusted
        image = ((image*255).astype(np.uint8))
    if ".tiff" in img:
        image = plt.imread(img)[:,:,:3]
        image = ((image*255).astype(np.uint8))
    return image

image = getUserImage()#Calling getImage function to get the image from the user

#PART 2
###############################################################################

def getKey(image, string): #Function generates the key for the user, image and key needed
    
    letters = len(string.replace(' ', '')) #removing spaces then calculating letter count
    
    x_r, x_c, x_l = image.shape #getting image dimensions and creating zeros array
    zero = np.zeros((x_r,x_c,x_l),dtype=int)
    
    for a in range(x_r): #for loop iterates through each element in the image to create the key
        for b in range(x_c):
            for c in range(x_l):
                A = (a * b) % letters #Calculations to create the key
                zero[a,b,c] = A*((2**8)//(letters))
    
    zero = zero.astype(np.uint8) #Applying .astype in case key array type is not uint8
    
    return zero
    

def decryptBlueDot(image, key):
    
    zero = image ^ key
    
    return zero

key = input("What is the key? ") #asking user for the key
keyArray = getKey(image,key)
decrypted = decryptBlueDot(image,keyArray)
plt.axis('off') #saving image without axises and whitespace as .tiff
plt.savefig('Decrypted_image.tiff',bbox_inches='tight')
plt.show()

input ("Part 2 Checkpoint")

#PART 3
###############################################################################

def grayscale(image):
    image = image.astype(np.float64) #change image type to float64
    #initialise RGB components
    R = image[:,:,0]
    G = image[:,:,1]
    B = image[:,:,2]
    grayscale_image = (0.299*R + 0.587*G + 0.114*B) #apply appropriate BT standard grayscale
    return grayscale_image

def gaussian_filter(image):
    input = ("Checkpoint 1")
    gaussian = ndimage.gaussian_filter(image, sigma=1.056) #apply gaussian filter to image
    plt.figure(1)
    plt.imshow(gaussian, cmap='gray')
    plt.title('Smooth & Gray Image')
    return gaussian

def sobel(image):
    image = image.astype(np.float64) #change image type to float64
    dx = ndimage.sobel(image,1)
    dy = ndimage.sobel(image,0)
    sobel_image = np.hypot(dx,dy) #find the value of the square root of the sums of the square of dx and dy
    plt.figure(2)
    plt.imshow(sobel_image,cmap='gray')
    plt.title('Sobel Operator Image')
    return sobel_image

def crop(image):
   
    maxintensity = 0 #initialize the value of maxintensity
    
    x_r, x_c, x_l = image.shape #for loop iterates through each element in the image to create the key
    
    for i in range(3, x_r - 3, 1):
        for j in range(3, x_c - 3, 1):#for loop to eliminate the edges
            if(image[i][j] > maxintensity):
                # if the pixel intensity is larger than the previous one, store it and its indices
                maxintensity = image[i][j] 
                i1 = i 
                j1 = j
   
    iLeft = i1-50
    jTop = j1+50
    
    crop = np.zeros(101,101) #initialize a new array
    for i in range(0, 101, 1):
        for j in range(0, 101, 1):
                crop[i][j] = image[iLeft + i ][jTop + j]  #centralize Earth and crop the image to 101 pixels.
    
    print(f"The Earth is located on row {i1}.")
    print(f"The Earth is located in column{j1}.")
    plt.imshow(crop,cmap='gray')
    plt.figure(3)
    plt.title('Earth location')
    return crop

grayscale(image)
gaussian_filter(image)
sobel(image)
crop(image)

#PART 4
###############################################################################

def getKeySpecial(image): #Function generates a an encryption/decryption key for the image
   
    string = input("What is the key? ") #asking user for the key
    letters = len(string.replace(' ', '')) #removing spaces then calculating letter count
    
    x_r, x_c, x_l = image.shape #creating zeroes array and getting image dimensions
    zero = np.zeros((x_r,x_c,x_l),dtype=int)
    
    for a in range(x_r): #For loop iterates through each color value in the image to generate an excryption key
        for b in range(x_c):
            for c in range(x_l):
                zero[a,b,c] = ((a ^ b) / letters)*((2**8)%(letters+11))
    
    zero = zero.astype(np.uint8) #Calling the astype function in case the key array is not the type uint8
   
    return zero
    
def encrypt(image, key): #Functuon XORs key with the image to encrypt it
    
    encrypt = image ^ key
    
    return encrypt

def pixelIntensity(image): #Funtcion prints the BGR intensities of the image in the argument
    plt.figure(101)
    plt.hist(image[:,:,0].reshape(image.shape[0]*image.shape[1]),bins=np.arange(2**8+1) , color = 'red')
    plt.figure(102)
    plt.hist(image[:,:,1].reshape(image.shape[0]*image.shape[1]),bins=np.arange(2**8+1) , color = 'green')
    plt.figure(103)
    plt.hist(image[:,:,2].reshape(image.shape[0]*image.shape[1]),bins=np.arange(2**8+1) , color = 'blue')
    plt.legend

keyArrayNew = getKeySpecial(image) #Calling the getKeySpecial function to creat an encryption key array
encrypted = encrypt(image,keyArray) #Generating the encrypted image
plt.figure(4)
plt.imshow(encrypted) #Plotting the encrypted image
pixelIntensity(image) #Plotting the RGB intensities of the original image (decrypted)