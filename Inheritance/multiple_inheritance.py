class Frontend:
  def frontend_skill(self):
    print("Frontend initialized.............")

class Backend:
  def backend_skill(self):
    print("Backend initialized.............")

class FullStack(Frontend,Backend):
  def fullstack_skill(self):
    print("can handle both frontend and backend")

f = FullStack()
f.frontend_skill()
f.backend_skill()
f.fullstack_skill()