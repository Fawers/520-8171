class KanbanError(Exception):
    pass

class ListNotFound(KanbanError):
    pass

class CardNotFound(KanbanError):
    pass
