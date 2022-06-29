package com.example.dependency.injection;

import lombok.RequiredArgsConstructor;

/**
 * AdvancedWizard implements inversion of control. It depends on abstraction that can be injected
 * through its constructor.
 */
@RequiredArgsConstructor
public class AdvancedWizard implements Wizard {

  private final Tobacco tobacco;

  @Override
  public void smoke() {
    tobacco.smoke(this);
  }
}
