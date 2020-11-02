from conans import ConanFile, tools

class OzoConan(ConanFile):
    name = "ozo"
    version = '0.0.1'
    license = 'Yandex LLC'
    url = 'https://github.com/yandex/ozo'
    description = 'Conan package for yandex ozo library.'
    settings = 'os', 'compiler', 'arch'
    generatos = 'cmake'

    def source(self):
        tools.get(self.url)

    def package(self):
        self.copy('include/*', src='ozo')

    def package_info(self):
        self.cpp_info.libs = ['ozo']
