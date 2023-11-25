import 'package:flame/components.dart';
import 'package:flame/collisions.dart';
import '../flapybirdGame.dart';

class wallBlock extends SpriteComponent with HasGameRef<flappyBirdGame> {
  //values
  final Vector2 gridPosition;
  double xOffset;
  final Vector2 velocity = Vector2.zero();

  //constructor
  wallBlock({
    required this.gridPosition,
    required this.xOffset,
  }) : super(size: Vector2.all(64), anchor: Anchor.bottomLeft);
  //methods
  @override
  void onLoad() {
    final platformImage = game.images.fromCache('block.png');
    sprite = Sprite(platformImage);
    position = Vector2(
      (gridPosition.x * size.x) + xOffset,
      game.size.y - (gridPosition.y * size.y),
    );
    add(RectangleHitbox(collisionType: CollisionType.passive));
  }

  @override
  void update(double dt) {
    velocity.x = game.objectSpeed;
    position += velocity * dt;

    if (position.x < -size.x) removeFromParent();
    super.update(dt);
  }
}
