import "package:flutter/material.dart";
import "package:flame/game.dart";

import 'flapybirdGame.dart';

void main() {
  final game = FlameGame();

  runApp(
    GameWidget<flappyBirdGame>.controlled(gameFactory: flappyBirdGame.new),
  );
}
