from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, ForeignKey, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime
import enum

Base = declarative_base()

class TransactionType(enum.Enum):
    PURCHASE = "purchase"
    REFUND = "refund"
    INVESTMENT = "investment"
    TRANSFER = "transfer"
    DEPOSIT = "deposit"
    WITHDRAWAL = "withdrawal"
    FEE = "fee"
    INTEREST = "interest"
    DIVIDEND = "dividend"

class BudgetPeriod(enum.Enum):
    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"
    QUARTERLY = "quarterly"
    YEARLY = "yearly"

class Account(Base):
    __tablename__ = "accounts"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    account_type = Column(String)  # checking, savings, credit_card
    bank = Column(String)  # chase, bofa, amex
    account_number_last4 = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    transactions = relationship("Transaction", back_populates="account")

class Transaction(Base):
    __tablename__ = "transactions"
    
    id = Column(Integer, primary_key=True, index=True)
    account_id = Column(Integer, ForeignKey("accounts.id"))
    date = Column(DateTime, index=True)
    description = Column(String)
    amount = Column(Float)
    transaction_type = Column(Enum(TransactionType), index=True)
    category = Column(String, index=True)
    subcategory = Column(String)
    is_duplicate = Column(Boolean, default=False)
    confidence_score = Column(Float)  # AI categorization confidence
    created_at = Column(DateTime, default=datetime.utcnow)
    
    account = relationship("Account", back_populates="transactions")

class Budget(Base):
    __tablename__ = "budgets"
    
    id = Column(Integer, primary_key=True, index=True)
    category = Column(String, index=True)
    limit = Column(Float)
    period = Column(Enum(BudgetPeriod), index=True)
    current_spent = Column(Float, default=0.0)
    start_date = Column(DateTime)  # Start of current budget period
    end_date = Column(DateTime)    # End of current budget period
    created_at = Column(DateTime, default=datetime.utcnow)