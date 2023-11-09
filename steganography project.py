import os
import cv2

# Function to hide a message within an image
def hide_message_in_image(image_path, message, password):
    img = cv2.imread(image_path)

    d = {}
    c = {}
    for i in range(255):
        d[chr(i)] = i
        c[i] = chr(i)

    n = 0
    m = 0
    z = 0

    for char in message:
        img[n, m, z] = d[char]
        n = n + 1
        m = m + 1
        z = (z + 1) % 3

    encrypted_image_path = "encrypted_image.png"
    cv2.imwrite(encrypted_image_path, img)
    os.startfile(encrypted_image_path)
    return encrypted_image_path

# Function to decrypt a message from an encrypted image
def decrypt_message_from_image(encrypted_image_path, password):
    img = cv2.imread(encrypted_image_path)

    d = {}
    c = {}
    for i in range(255):
        d[chr(i)] = i
        c[i] = chr(i)

    decrypted_message = ""  # Use a different variable for building the decrypted message
    n = 0
    m = 0
    z = 0

    for i in range(len(message)):
        decrypted_message = decrypted_message + c[img[n, m, z]]
        n = n + 1
        m = m + 1
        z = (z + 1) % 3

    return decrypted_message

# Main code
if __name__ == "__main__":
    image_path = "pic.jpeg"
    message = input("Enter your message: ")
    password = input("Enter password: ")

    encrypted_image_path = hide_message_in_image(image_path, message, password)
    print("Message successfully hidden in the image.")

    pas = input("Enter password for decryption: ")
    if password == pas:
        decrypted_message = decrypt_message_from_image(encrypted_image_path, password)
        print("Decrypted message:", decrypted_message)
    else:
        print("You are not authenticated.")
