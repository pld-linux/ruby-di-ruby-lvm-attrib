#!/bin/sh
# Creates branch for GitHub PR to submit upstream new LVM version attributes
# Version is taken as version of device-mapper-devel package
#
# Usage:
# ./pld-update-attributes.sh
# Author: Elan Ruusamäe <glen@pld-linux.org>
#

git_url=git@github.com:gregsymons/di-ruby-lvm-attrib.git
dir=di-ruby-lvm-attrib
set -e

if [ ! -d "$dir" ]; then
	git clone $git_url $dir --depth=1
fi

cd $dir

git checkout next
git pull --rebase
lvm_version=$(rpm -q device-mapper-devel --qf '%{V}')
tag_ver=v$(echo "$lvm_version" | tr . _)

./update-lvm.sh "$tag_ver"

lvm_dir=$(ls -d "$lvm_version("*")-git")
attr_dir=lib/lvm/attributes/${lvm_dir%-git}
mv $lvm_dir $attr_dir

git add -A $attr_dir
git checkout -b LVM-$lvm_version
git commit -am "Added $lvm_version attributes"
