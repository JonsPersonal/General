

export default restart => {
    let engine = Matter.Engine.create({enableSleeping:false});
    let world = engine.world;
    engine.gravity = 0.4;

    return{
        physics:{engine,world}
    }
}