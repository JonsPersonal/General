import 'package:flame/components.dart';
import 'package:flame/input.dart';
import '../flapybirdGame.dart';

class birdPlayer extends SpriteAnimationComponent
    with HasGameRef<flappyBirdGame> {
  final double gravity = 15;
  final double moveSpeed = 100;
  final Vector2 velocity = Vector2.zero();
  double jumpSpeed = 0;
  birdPlayer({
    required super.position,
  }) : super(size: Vector2.all(64), anchor: Anchor.center);

  @override
  void onLoad() {
    animation = SpriteAnimation.fromFrameData(
      game.images.fromCache("ember.png"),
      SpriteAnimationData.sequenced(
          amount: 4, stepTime: 0.12, textureSize: Vector2.all(16)),
    );
  }

  @override
  void update(double dt) {
    // Prevent ember from going beyond half screen.

    if (position.x + 64 >= game.size.x / 2) {
      velocity.x = 0;
      game.objectSpeed = -moveSpeed;
    } else {
      velocity.x = moveSpeed;
    }

    velocity.y += gravity - jumpSpeed;
    if (jumpSpeed > 0) {
      jumpSpeed = jumpSpeed - gravity;
    }

    position += velocity * dt;

    if (position.x < -size.x) removeFromParent();
    super.update(dt);
  }

  void jump() {
    if (jumpSpeed < 600) {
      jumpSpeed += 60;
    }
  }
}
