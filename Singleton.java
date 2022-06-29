package com.example.singleton;

/**
 * Singleton class. Eagerly initialized static instance guarantees thread safety.
 */
public final class ExampleSingleton {

  /**
   * Private constructor so nobody can instantiate the class.
   */
  private ExampleSingleton() {
  }

  /**
   * Static to class instance of the class.
   */
  private static final ExampleSingleton INSTANCE = new ExampleSingleton();

  /**
   * To be called by user to obtain instance of the class.
   *
   * @return instance of the singleton.
   */
  public static ExampleSingleton getInstance() {
    return INSTANCE;
  }
}
