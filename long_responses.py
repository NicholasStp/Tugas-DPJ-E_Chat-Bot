import random

R_EATING = "Saya tidak suka makan apa pun karena saya adalah program komputer!"
R_ADVICE = "Jika saya jadi Anda, saya akan membuka internet dan mengetik persis apa yang Anda tulis di sana!"


def unknown():
    response = ["Bisakah Anda ulangi kalimatnya? ",
                "...",
                "Kedengarannya seperti itu",
                "Apa yang maksudnya?"][
        random.randrange(4)]
    return response