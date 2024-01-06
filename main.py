def on_a_pressed():
    duck.start_effect(effects.rings, randint(100, 600))
    music.play_melody("E D G F B A C5 B ", 500)
    music.play_melody("E B C5 A B G A F ", 519)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

duck: Sprite = None
scene.set_background_color(10)
game.splash("Hi there, cool stuff *** !!! :)")
duck = sprites.create(img("""
        . . . . . . . . . . b 5 b . . . 
            . . . . . . . . . b 5 b . . . . 
            . . . . . . b b b b b b . . . . 
            . . . . . b b 5 5 5 5 5 b . . . 
            . . . . b b 5 d 1 f 5 d 4 c . . 
            . . . . b 5 5 1 f f d d 4 4 4 b 
            . . . . b 5 5 d f b 4 4 4 4 b . 
            . . . b d 5 5 5 5 4 4 4 4 b . . 
            . b b d d d 5 5 5 5 5 5 5 b . . 
            b d d d b b b 5 5 5 5 5 5 5 b . 
            c d d b 5 5 d c 5 5 5 5 5 5 b . 
            c b b d 5 d c d 5 5 5 5 5 5 b . 
            c b 5 5 b c d d 5 5 5 5 5 5 b . 
            b b c c c d d d 5 5 5 5 5 d b . 
            . . . . c c d d d 5 5 5 b b . . 
            . . . . . . c c c c c b b . . .
    """),
    SpriteKind.food)