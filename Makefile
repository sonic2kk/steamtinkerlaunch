ifeq ($(PREFIX),)
    PREFIX := /usr
endif

.PHONY: build install

build:

install:
	install -Dm755 stl -t "$(PREFIX)/bin"

	install -d "$(PREFIX)/share/stl"
	cp -r categories lang misc regs reshadepresets tweaks "$(PREFIX)/share/stl"

	install -Dm644 README.md -t "$(PREFIX)/share/doc/steamtinkerlaunch"

