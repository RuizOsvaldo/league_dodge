scene.set_background_color(9)
# Player
player = sprites.create(img("""
        . . . . f f f f f . . . . . . .
        . . . f e e e e e f . . . . . .
        . . f d d d d e e e f . . . . .
        . c d f d d f d e e f f . . . .
        . c d f d d f d e e d d f . . .
        c d e e d d d d e e b d c . . .
        c d d d d c d d e e b d c . f f
        c c c c c d d d e e f c . f e f
        . f d d d d d e e f f . . f e f
        . . f f f f f e e e e f . f e f
        . . . . f e e e e e e e f f e f
        . . . f e f f e f e e e e f f .
        . . . f e f f e f e e e e f . .
        . . . f d b f d b f f e f . . .
        . . . f d d c d d b b d f . . .
        . . . . f f f f f f f f f . . .
        """),
    SpriteKind.player)
controller.move_sprite(player, 100, 0)
player.set_stay_in_screen(True)
player.set_position(80, 101)
# Lives
info.set_life(3)
# Enemy spawn

def on_update_interval():
    enemy = sprites.create(img("""
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . c c . . . . . . . .
            . . . . c a f b c . . . . . . .
            . . . . b f f b c c . . . . . .
            . . . a a f b a b a c . . . . .
            . . . c a c b b f f b . . . . .
            . . . . b f f b f a b . . . . .
            . . . . a f f b b b a . . . . .
            . . . . . a b b c c . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            """),
        SpriteKind.enemy)
    enemy.set_position(randint(0, scene.screen_width()), 0)
    enemy.vy = randint(30, 70)
game.on_update_interval(500, on_update_interval)

# Collision handling

def on_on_overlap(sprite, enemy2):
    sprites.destroy(enemy2, effects.fire, 100)
    info.change_life_by(-1)
    pause(1000)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap)
