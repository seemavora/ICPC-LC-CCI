
public class LightBulb {
    public void light() {
        System.out.println("lighting a room");
    }
}

class SmartBulb extends LightBulb {
    @Override
    public void light() {
        System.out.println("doing everything in a smart way");
    }
}

class BulbTester {
    public static void main(String[] args) {
        SmartBulb smart = new SmartBulb();
        LightBulb bulb = smart;

        bulb.light();
    }
}