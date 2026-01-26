scene.setBackgroundColor(9)

// Player
let player = sprites.create(img`
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
`, SpriteKind.Player)

controller.moveSprite(player, 100, 0)
player.setStayInScreen(true)
player.setPosition(80, 101)

// Lives
info.setLife(3)

// Enemy spawn
game.onUpdateInterval(500, function () {
    let enemy = sprites.create(img`
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
    `, SpriteKind.Enemy)

    enemy.setPosition(randint(0, scene.screenWidth()), 0)
    enemy.vy = randint(30, 70)
})

// Collision handling
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite, enemy) {
    sprites.destroy(enemy, effects.fire, 100)
    info.changeLifeBy(-1)
    pause(1000)
})

