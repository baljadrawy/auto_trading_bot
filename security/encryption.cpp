#include <openssl/evp.h>
#include <openssl/rand.h>
#include <iostream>
#include <fstream>

void encryptData(const std::string& plaintext, std::string& ciphertext) {
    // تنفيذ تشفير البيانات باستخدام OpenSSL
    EVP_CIPHER_CTX* ctx = EVP_CIPHER_CTX_new();
    if(!ctx) {
        std::cerr << "خطأ: لم يتمكن من إنشاء سياق التشفير" << std::endl;
        return;
    }

    // إعداد المفتاح والـ IV
    unsigned char key[EVP_MAX_KEY_LENGTH];
    unsigned char iv[EVP_MAX_IV_LENGTH];
    RAND_bytes(key, sizeof(key));
    RAND_bytes(iv, sizeof(iv));

    // بدء عملية التشفير
    if(!EVP_EncryptInit_ex(ctx, EVP_aes_256_cbc(), nullptr, key, iv)) {
        std::cerr << "خطأ: لم يتمكن من بدء عملية التشفير" << std::endl;
        EVP_CIPHER_CTX_free(ctx);
        return;
    }

    // تنفيذ التشفير
    unsigned char outbuf[1024];
    int outlen;
    if(!EVP_EncryptUpdate(ctx, outbuf, &outlen, reinterpret_cast<const unsigned char*>(plaintext.c_str()), plaintext.size())) {
        std::cerr << "خطأ: فشل في تحديث التشفير" << std::endl;
        EVP_CIPHER_CTX_free(ctx);
        return;
    }
    ciphertext.assign(reinterpret_cast<char*>(outbuf), outlen);

    // إنهاء التشفير
    if(!EVP_EncryptFinal_ex(ctx, outbuf, &outlen)) {
        std::cerr << "خطأ: فشل في إنهاء التشفير" << std::endl;
    } else {
        ciphertext.append(reinterpret_cast<char*>(outbuf), outlen);
    }

    EVP_CIPHER_CTX_free(ctx);
}

int main() {
    std::string plaintext = "هذا هو النص الذي سيتم تشفيره";
    std::string ciphertext;
    encryptData(plaintext, ciphertext);

    std::ofstream file("encrypted_data.bin", std::ios::binary);
    file.write(ciphertext.data(), ciphertext.size());
    file.close();

    std::cout << "تم تشفير البيانات وتخزينها بنجاح" << std::endl;
    return 0;
}
