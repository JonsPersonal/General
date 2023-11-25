import 'package:flame/events.dart';
import 'package:flutter/material.dart';
import 'package:flame/components.dart';
import 'package:flame/game.dart';

import 'managers/segmentManager.dart';
import 'package:flappy_clone/actors/bird.dart';
import 'package:flappy_clone/objects/ground.dart';
import 'package:flappy_clone/objects/wall.dart';

class flappyBirdGame extends FlameGame with TapDetector {
  flappyBirdGame();

  final world = World();
  late final CameraComponent camera;
  late birdPlayer _bird;

  double objectSpeed = 0.0;

  @override
  Future<void> onLoad() async {
    await images.loadAll(['block.png', 'ember.png', 'ground.png']);
    camera = CameraComponent(world: world);
    camera.viewfinder.anchor = Anchor.topLeft;

    addAll([camera, world]);

    initializeGame();
  }

// deals with the infinite map segments
  void loadGameSegments(int segmentIndex, double xOffset) {
    for (final block in segments[segmentIndex]) {
      switch (block.blockType) {
        case wallBlock:
          add(wallBlock(gridPosition: block.gridPosition, xOffset: xOffset));
          break;
        case groundBlock:
          break;
      }
    }
  }

  void initializeGame() {
    final segmentsToLoad = (size.x / 320).ceil();

    segmentsToLoad.clamp(0, segments.length);

    for (var i = 0; i <= segmentsToLoad; i++) {
      loadGameSegments(i, (320 * i).toDouble());
    }

    //adding player
    _bird = birdPlayer(position: Vector2(128, canvasSize.y - 70));
    world.add(_bird);
  }

  @override
  Color backgroundColor() {
    return const Color.fromARGB(255, 173, 223, 247);
  }

  @override
  void onTap() {
    print("i jump!");
    _bird.jump();
  }
}
