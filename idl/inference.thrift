struct Picture{
    1: binary origin;
    2: i32 width;
    3: i32 depth;
}

struct Order{
    1: list<double> orders;
}

service Inference{
    Order sendPhoto(1:Picture picture),
}
