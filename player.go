package main

import (
	"github.com/veandco/go-sdl2/sdl"
)

const (
	speed = 0.02
)

type player struct {
	tex *sdl.Texture

	x, y float64
}

func newPlayer(renderer *sdl.Renderer) (p player, err error) {
	p.tex = textureFromPNG(renderer, "sprites/player.png")
	return p, nil
}

func (p *player) draw(renderer *sdl.Renderer) {
	renderer.Copy(p.tex,
		&sdl.Rect{X: 0, Y: 0, W: 6, H: 12},
		&sdl.Rect{X: int32(p.x), Y: int32(p.y), W: 60, H: 120})
}
func (p *player) update() {
	keys := sdl.GetKeyboardState()

	if keys[sdl.SCANCODE_W] == 1 {
		//move player up
		p.y -= speed
	}
	if keys[sdl.SCANCODE_A] == 1 {
		//move player up
		p.x -= speed
	}
	if keys[sdl.SCANCODE_S] == 1 {
		//move player up
		p.y += speed
	}
	if keys[sdl.SCANCODE_D] == 1 {
		//move player up
		p.x += speed
	}

}

/*
switch uint8(1) {
case keys[sdl.SCANCODE_W]:
	//move player up
	p.y -= speed
	fallthrough
case keys[sdl.SCANCODE_A]:
	//move player left
	p.x -= speed
	fallthrough
case keys[sdl.SCANCODE_S]:
	//move player down
	p.y += speed
	fallthrough
case keys[sdl.SCANCODE_D]:
	//move player right
	p.x += speed
}
*/
