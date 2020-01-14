from mediate.errors import *


class CornerstoneError(MediateError):
    uni_name = "CornerStoneError"  # cornerstone error


err_count = count(1)
UNBOUND_USER = CornerstoneError(next(err_count))
ALLREADY_REGISTER_USER = CornerstoneError(next(err_count))
CORNERSTONE_NOT_BOUGHT = CornerstoneError(next(err_count))
INCOMPLETE_COURSE = CornerstoneError(next(err_count))
TASK_ALREADY_USE = CornerstoneError(next(err_count))
MUTIPLE_FRIEND = CornerstoneError(next(err_count))
INVALID_USER_PRIVILEGE = CornerstoneError(next(err_count))
FINISHED_SESSION = CornerstoneError(next(err_count))
EXCEEDED_CHAPTER = CornerstoneError(next(err_count))
NO_EXAM = CornerstoneError(next(err_count))
EXISTENT_EXAM = CornerstoneError(next(err_count))
INADEQUATE_SCORE = CornerstoneError(next(err_count))
EXAM_TIMEOUT = CornerstoneError(next(err_count))
STRANGE_ANSWERS = CornerstoneError(next(err_count))

# roadmap
ROADMAP_AREADY_USE = CornerstoneError(next(err_count))
POST_EMPTY_JSON = CornerstoneError(next(err_count))
EXCEEDED_NODE_LENGTH = CornerstoneError(next(err_count))
DUPLICATED_COURSE = CornerstoneError(next(err_count))