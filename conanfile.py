from conans import ConanFile, tools

class OzoConan(ConanFile):
    name = "ozo"
    version = '0.1.0'
    license = 'Yandex LLC'
    url = 'https://github.com/yandex/ozo'
    description = 'Conan package for yandex ozo library.'
    generatos = 'cmake'

    def source(self):
        git = tools.Git(folder='ozo')
        git.clone(self.url, branch='master')
        git.run('submodule update --init --recursive')

    def package(self):
        self.copy('include/*.h', src='ozo')
        self.copy('include/*.hpp', src='ozo')
        self.copy('contrib/*.hpp', src='ozo')
        self.copy('contrib/*.h', src='ozo')
        self.copy('contrib/*.dat', src='ozo')

    def package_info(self):
        self.cpp_info.includedirs = ['include/', 'contrib/resource_pool/include/']

