#include <iostream>
#include <fstream>
#include <map>
#include <string>

// Clase que representa un archivo en el sistema de archivos simulado
class File {
public:
    std::string name;
    std::string content;

    File(const std::string& name, const std::string& content) : name(name), content(content) {}
};

// Clase que representa un sistema de archivos simple
class SimpleFileSystem {
private:
    std::map<std::string, File> files; // Mapa para almacenar archivos con su nombre como clave

public:
    // Crear un nuevo archivo
    void createFile(const std::string& name, const std::string& content) {
        if (files.find(name) != files.end()) {
            std::cerr << "Error: File already exists.\n";
            return;
        }
        files[name] = File(name, content);
        std::cout << "File created: " << name << "\n";
    }

    // Leer el contenido de un archivo
    void readFile(const std::string& name) {
        auto it = files.find(name);
        if (it == files.end()) {
            std::cerr << "Error: File not found.\n";
            return;
        }
        std::cout << "File content of " << name << ": " << it->second.content << "\n";
    }

    // Escribir o actualizar el contenido de un archivo
    void writeFile(const std::string& name, const std::string& content) {
        auto it = files.find(name);
        if (it == files.end()) {
            std::cerr << "Error: File not found.\n";
            return;
        }
        it->second.content = content;
        std::cout << "File updated: " << name << "\n";
    }

    // Eliminar un archivo
    void deleteFile(const std::string& name) {
        auto it = files.find(name);
        if (it == files.end()) {
            std::cerr << "Error: File not found.\n";
            return;
        }
        files.erase(it);
        std::cout << "File deleted: " << name << "\n";
    }
};

int main() {
    SimpleFileSystem sfs;

    // Ejemplo de uso
    sfs.createFile("example.txt", "This is a test file.");
    sfs.readFile("example.txt");
    sfs.writeFile("example.txt", "Updated content.");
    sfs.readFile("example.txt");
    sfs.deleteFile("example.txt");
    sfs.readFile("example.txt");

    return 0;
}
