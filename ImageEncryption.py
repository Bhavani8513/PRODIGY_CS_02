from PIL import Image

def encrypt_image(imagepath, key):
    image = Image.open(imagepath)
    pixels = list(image.getdata())
    encrypted_pixels = []

    for pixel in pixels:
        r, g, b = pixel
        encrypted_r = (r + key) % 256
        encrypted_g = (g + key) % 256
        encrypted_b = (b + key) % 256
        encrypted_pixels.append((encrypted_r, encrypted_g, encrypted_b))

    encrypted_image = Image.new(image.mode, image.size)
    encrypted_image.putdata(encrypted_pixels)
    encrypted_image.save("encrypted_image.png")

def decrypt_image(image_path, key):
    image = Image.open(image_path)
    pixels = list(image.getdata())
    decrypted_pixels = []

    for pixel in pixels:
        r, g, b = pixel
        decrypted_r = (r - key) % 256
        decrypted_g = (g - key) % 256
        decrypted_b = (b - key) % 256
        decrypted_pixels.append((decrypted_r, decrypted_g, decrypted_b))

    decrypted_image = Image.new(image.mode, image.size)
    decrypted_image.putdata(decrypted_pixels)
    decrypted_image.save("decrypted_image.png")

def main():
    while True:
        print("Image Encryption And Manipulation")
        print("1. Encrypt an image")
        print("2. Decrypt an image")
        print("3. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            image_path = input("Enter the image path: ")
            key = int(input("Enter the encryption key: "))
            encrypt_image(image_path, key)
            print("Image encrypted successfully!")
        elif choice == "2":
            image_path = input("Enter the encrypted image path: ")
            key = int(input("Enter the decryption key: "))
            decrypt_image(image_path, key)
            print("Image decrypted successfully!")
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()