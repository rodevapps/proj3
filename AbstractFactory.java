package com.example.abstractfactory;

import lombok.Getter;
import lombok.Setter;

/**
 * King interface.
 */
public interface King {

  String getDescription();
}

/**
 * Army interface.
 */
public interface Army {

  String getDescription();
}

/**
 * Castle interface.
 */
public interface Castle {

  String getDescription();
}

/**
 * KingdomFactory factory interface.
 */
public interface KingdomFactory {

  Castle createCastle();

  King createKing();

  Army createArmy();

}

/**
 * ElfKingdomFactory concrete factory.
 */
public class ElfKingdomFactory implements KingdomFactory {

  @Override
  public Castle createCastle() {
    return new ElfCastle();
  }

  @Override
  public King createKing() {
    return new ElfKing();
  }

  @Override
  public Army createArmy() {
    return new ElfArmy();
  }

}

/**
 * OrcKingdomFactory concrete factory.
 */
public class OrcKingdomFactory implements KingdomFactory {

  @Override
  public Castle createCastle() {
    return new OrcCastle();
  }

  @Override
  public King createKing() {
    return new OrcKing();
  }

  @Override
  public Army createArmy() {
    return new OrcArmy();
  }
}

/**
 * ElfArmy.
 */
public class ElfArmy implements Army {

  static final String DESCRIPTION = "This is the elven army!";

  @Override
  public String getDescription() {
    return DESCRIPTION;
  }
}

/**
 * ElfCastle.
 */
public class ElfCastle implements Castle {

  static final String DESCRIPTION = "This is the elven castle!";

  @Override
  public String getDescription() {
    return DESCRIPTION;
  }
}

/**
 * ElfKing.
 */
public class ElfKing implements King {

  static final String DESCRIPTION = "This is the elven king!";

  @Override
  public String getDescription() {
    return DESCRIPTION;
  }
}

/**
 * OrcArmy.
 */
public class OrcArmy implements Army {

  static final String DESCRIPTION = "This is the elven army!";

  @Override
  public String getDescription() {
    return DESCRIPTION;
  }
}

/**
 * OlcCastle.
 */
public class OrcCastle implements Castle {

  static final String DESCRIPTION = "This is the elven castle!";

  @Override
  public String getDescription() {
    return DESCRIPTION;
  }
}

/**
 * OrcKing.
 */
public class OrcKing implements King {

  static final String DESCRIPTION = "This is the elven king!";

  @Override
  public String getDescription() {
    return DESCRIPTION;
  }
}


@Getter
@Setter
public class Kingdom {

  private King king;
  private Castle castle;
  private Army army;

  /**
   * The factory of kingdom factories.
   */
  public static class FactoryMaker {

    /**
     * Enumeration for the different types of Kingdoms.
     */
    public enum KingdomType {
      ELF, ORC
    }

    /**
     * The factory method to create KingdomFactory concrete objects.
     */
    public static KingdomFactory makeFactory(KingdomType type) {
      switch (type) {
        case ELF:
          return new ElfKingdomFactory();
        case ORC:
          return new OrcKingdomFactory();
        default:
          throw new IllegalArgumentException("KingdomType not supported.");
      }
    }
  }
}
