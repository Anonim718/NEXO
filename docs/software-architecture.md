# NEXO Software Architecture

NEXO keeps three concerns separate:

1. **Safety:** Brain and Arduino decide whether motion is allowed.
2. **Execution:** Planner and Bridge turn approved intent into controller actions.
3. **Experience:** Voice, memory, behaviour and future AI provide interaction without bypassing safety.

This separation means personality can change without changing motor safety, and
AI providers can change without changing the physical controller contract.
