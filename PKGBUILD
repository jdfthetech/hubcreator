pkgname=hubcreator
pkgver=0.0.1
pkgrel=1
pkgdesc="hubcreator binary for making github repos"
arch=('x86_64')
url="https://github.com/jdfthetech/hubcreator"
license=('GPL2')
provides=('hubcreator')

source_x86_64=("https://github.com/jdfthetech/hubcreator/releases/download/hubcreator-linux-0.0.1/hubcreator")
noextract=("hubcreator")
sha256sums_x86_64=('b93bdb484bd60e54d56d0bceaf4f3bcb315d85ae3fd8ee519fe98f745361952f')

package () {
  install -Dm 775 "hubcreator" "${pkgdir}/usr/bin/hubcreator"
}

