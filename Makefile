ifeq ($(PREFIX),)
    PREFIX := /usr
endif

.PHONY: build install

build:

install:
	sed "s:^PREFIX=\"/usr\":PREFIX=\"$(PREFIX)\":" -i stl
	install -Dm755 stl -t "$(PREFIX)/bin"

	install -d "$(PREFIX)/share/stl"
	cp -r categories eval guicfgs lang misc reshadepresets "$(PREFIX)/share/stl"

	install -Dm644 README.md -t "$(PREFIX)/share/doc/steamtinkerlaunch"

