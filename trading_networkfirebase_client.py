"""
Firebase client for real-time state management and data persistence.
Implements retry logic, connection pooling, and error recovery.
"""
import firebase_admin
from firebase_admin import credentials, firestore, exceptions
from google.cloud.firestore_v1.client import Client as FirestoreClient
from google.cloud.firestore_v1.document import DocumentReference
from typing import Dict, Any, Optional, List, Callable
import threading
import time
import logging
from datetime import datetime
from queue import Queue, Empty

logger = logging.getLogger(__name__)

class FirebaseClient:
    """Managed Firebase client with automatic reconnection"""
    
    _instance = None