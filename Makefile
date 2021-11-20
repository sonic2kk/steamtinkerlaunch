ifeq ($(PREFIX),)
    PREFIX := /usr
endif

.PHONY: build install

build:

install:
	sed "s:^PREFIX=\"/usr\":PREFIX=\"$(PREFIX)\":" -i steamtinkerlaunch
	install -Dm755 steamtinkerlaunch -t "$(PREFIX)/bin"

	install -d "$(PREFIX)/share/steamtinkerlaunch"
	cp -r categories eval guicfgs lang misc "$(PREFIX)/share/steamtinkerlaunch"

	install -Dm644 README.md -t "$(PREFIX)/share/doc/steamtinkerlaunch"
	install -Dm644 "misc/steamtinkerlaunch.desktop" -t "$(PREFIX)/share/applications"
	install -Dm644 "misc/steamtinkerlaunch.svg" -t "$(PREFIX)/share/icons/hicolor/scalable/apps"

