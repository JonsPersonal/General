import 'package:flame/components.dart';
import 'package:flappy_clone/objects/ground.dart';
import 'package:flappy_clone/objects/wall.dart';

class Block {
  final Vector2 gridPosition;
  final Type blockType;
  Block(this.gridPosition, this.blockType);
}

final segments = [segment0, segment1, segment2, segment3];

final segment0 = [
  Block(Vector2(0, 0), groundBlock),
  Block(Vector2(1, 0), groundBlock),
  Block(Vector2(2, 0), groundBlock),
  Block(Vector2(3, 0), groundBlock),
  Block(Vector2(4, 0), groundBlock),
  Block(Vector2(4, 1), wallBlock),
  Block(Vector2(4, 2), wallBlock),
  Block(Vector2(4, 3), wallBlock),
  Block(Vector2(4, 4), wallBlock),
];
final segment1 = [
  Block(Vector2(0, 0), groundBlock),
  Block(Vector2(1, 0), groundBlock),
  Block(Vector2(2, 0), groundBlock),
  Block(Vector2(3, 0), groundBlock),
  Block(Vector2(4, 0), groundBlock),
  Block(Vector2(4, 10), wallBlock),
  Block(Vector2(4, 9), wallBlock),
  Block(Vector2(4, 8), wallBlock),
  Block(Vector2(4, 7), wallBlock),
];

final segment2 = [
  Block(Vector2(0, 0), groundBlock),
  Block(Vector2(1, 0), groundBlock),
  Block(Vector2(2, 0), groundBlock),
  Block(Vector2(3, 0), groundBlock),
  Block(Vector2(4, 0), groundBlock),
  Block(Vector2(4, 1), wallBlock),
  Block(Vector2(4, 2), wallBlock),
  Block(Vector2(4, 3), wallBlock),
];

final segment3 = [
  Block(Vector2(0, 0), groundBlock),
  Block(Vector2(1, 0), groundBlock),
  Block(Vector2(2, 0), groundBlock),
  Block(Vector2(3, 0), groundBlock),
  Block(Vector2(4, 0), groundBlock),
  Block(Vector2(4, 10), wallBlock),
  Block(Vector2(4, 9), wallBlock),
  Block(Vector2(4, 8), wallBlock),
];
