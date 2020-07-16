package main

import (
	"fmt"

	"github.com/veandco/go-sdl2/sdl"

	"github.com/veandco/go-sdl2/img"
)

func main() {

	if err := sdl.Init(sdl.INIT_EVERYTHING); err != nil {
		fmt.Println("initializing sdl:", err)
		return
	}

	img.Init(img.INIT_PNG)

	window, err := sdl.CreateWindow(
		"Divel: wip game",
		sdl.WINDOWPOS_UNDEFINED, sdl.WINDOWPOS_UNDEFINED,
		854, 300,
		sdl.WINDOW_OPENGL)

	if err != nil {
		fmt.Println("initializing window:", err)
		return
	}
	defer window.Destroy()

	renderer, err := sdl.CreateRenderer(window, -1, sdl.RENDERER_ACCELERATED)
	if err != nil {
		fmt.Println("initializing renderer:", err)
		return
	}
	defer renderer.Destroy()

	img, err := img.Load("sprites/player.png")
	if err != nil {
		fmt.Println("loading sprites:", err)
		return
	}

	for {
		for event := sdl.PollEvent(); event != nil; event = sdl.PollEvent() {
			switch event.(type) {
			case *sdl.QuitEvent:
				return
			}
		}
		renderer.SetDrawColor(33, 36, 61, 255)
		renderer.Clear()

		renderer.Present()
	}
}
