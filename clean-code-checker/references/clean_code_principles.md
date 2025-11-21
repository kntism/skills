# Clean Code Principles and Guidelines

This document provides comprehensive guidance for Clean Code principles that the Clean Code Checker skill implements.

## Core Clean Code Principles

### 1. Naming Conventions

#### JavaScript/TypeScript
- **camelCase** for variables, functions, and properties
- **PascalCase** for classes and constructors
- **UPPER_CASE** for constants

**Examples:**
```javascript
// Good
const userName = "John";
function calculateTotal(items) { ... }
class UserProfile { ... }
const MAX_ATTEMPTS = 3;

// Bad
const user_name = "John";
function CalculateTotal(items) { ... }
class userProfile { ... }
const maxAttempts = 3;
```

#### Python
- **snake_case** for variables, functions, and methods
- **PascalCase** for classes
- **UPPER_CASE** for constants

**Examples:**
```python
# Good
user_name = "John"
def calculate_total(items): ...
class UserProfile: ...
MAX_ATTEMPTS = 3

# Bad
userName = "John"
def CalculateTotal(items): ...
class user_profile: ...
maxAttempts = 3
```

### 2. Function Design

#### Key Principles
- **Small functions** (under 20 lines)
- **Single responsibility** - one purpose per function
- **Few parameters** (prefer 3 or fewer)
- **No side effects** - pure functions when possible

#### JavaScript/TypeScript
```javascript
// Good - small, focused function
function validateEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

// Bad - large function with multiple responsibilities
function processUserData(userData) {
    // Validate user data
    if (!userData.email || !userData.password) {
        throw new Error("Missing required fields");
    }

    // Process email
    const processedEmail = userData.email.toLowerCase().trim();

    // Hash password
    const hashedPassword = hashPassword(userData.password);

    // Create user object
    const user = {
        email: processedEmail,
        password: hashedPassword,
        createdAt: new Date(),
        updatedAt: new Date()
    };

    // Save to database
    saveUser(user);

    return user;
}
```

#### Python
```python
# Good - small, focused function
def validate_email(email: str) -> bool:
    """Validate email format."""
    email_regex = r'^[^\s@]+@[^\s@]+\.[^\s@]+$'
    return re.match(email_regex, email) is not None

# Bad - large function with multiple responsibilities
def process_user_data(user_data):
    """Process user data (violates multiple principles)."""
    # Validate user data
    if not user_data.get('email') or not user_data.get('password'):
        raise ValueError("Missing required fields")

    # Process email
    processed_email = user_data['email'].lower().strip()

    # Hash password
    hashed_password = hash_password(user_data['password'])

    # Create user object
    user = {
        'email': processed_email,
        'password': hashed_password,
        'created_at': datetime.now(),
        'updated_at': datetime.now()
    }

    # Save to database
    save_user(user)

    return user
```

### 3. Comments

#### Good Comments
- **Explain WHY**, not WHAT
- **Provide context** that isn't obvious
- **Keep comments updated** with code changes

**Examples:**
```javascript
// Good - explains why we use this specific algorithm
function calculateTax(income, region) {
    // Use progressive tax rates for better income distribution
    const rates = getProgressiveRates(region);
    return applyProgressiveTax(income, rates);
}

// Bad - just restates what the code does
function calculateTax(income, region) {
    // Calculate tax based on income and region
    return income * 0.15; // 15% tax rate
}
```

#### Comments to Avoid
- **Obvious comments** that just repeat the code
- **Dead code** (commented-out code)
- **Misleading comments** that don't match the code

### 4. Code Formatting

#### Line Length
- **Maximum 80-100 characters** per line
- **Break long lines** at logical points
- **Use proper indentation** (2 or 4 spaces)

#### JavaScript/TypeScript
```javascript
// Good
const userMessage = `Welcome back, ${userName}! You have ${unreadCount} unread messages.`;

// Bad
const userMessage = "Welcome back, " + userName + "! You have " + unreadCount + " unread messages.";
```

#### Python
```python
# Good
user_message = f"Welcome back, {user_name}! You have {unread_count} unread messages."

# Bad
user_message = "Welcome back, " + user_name + "! You have " + unread_count + " unread messages."
```

### 5. Error Handling

#### JavaScript/TypeScript
```javascript
// Good - specific error handling
function processFile(filePath) {
    try {
        const content = fs.readFileSync(filePath, 'utf8');
        return parseJSON(content);
    } catch (error) {
        if (error.code === 'ENOENT') {
            throw new FileNotFoundError(`File not found: ${filePath}`);
        } else if (error instanceof SyntaxError) {
            throw new JSONParseError(`Invalid JSON format: ${error.message}`);
        }
        throw error;
    }
}

// Bad - generic error handling
function processFile(filePath) {
    try {
        const content = fs.readFileSync(filePath, 'utf8');
        return parseJSON(content);
    } catch (error) {
        console.log('Error occurred');
        throw error;
    }
}
```

#### Python
```python
# Good - specific error handling
def process_file(file_path):
    """Process file with proper error handling."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return json.loads(content)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON format: {e}")
    except Exception as e:
        raise RuntimeError(f"Unexpected error processing file: {e}")

# Bad - bare except
def process_file(file_path):
    """Process file with poor error handling."""
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return json.loads(content)
    except:
        print("Error occurred")
        raise
```

### 6. Code Duplication

#### Prevention Strategies
- **Extract common functionality** to reusable functions
- **Use composition** over inheritance where appropriate
- **Create utility modules** for shared operations

**Example:**
```javascript
// Bad - duplicate code
function processUser(user) {
    const userData = {
        id: user.id,
        name: user.name,
        email: user.email,
        createdAt: new Date()
    };
    saveToDatabase(userData);
    return userData;
}

function processAdmin(admin) {
    const adminData = {
        id: admin.id,
        name: admin.name,
        email: admin.email,
        role: 'admin',
        createdAt: new Date()
    };
    saveToDatabase(adminData);
    return adminData;
}

// Good - extracted common functionality
function createUserData(user, role = 'user') {
    return {
        id: user.id,
        name: user.name,
        email: user.email,
        role: role,
        createdAt: new Date()
    };
}

function processUser(user) {
    const userData = createUserData(user);
    saveToDatabase(userData);
    return userData;
}

function processAdmin(admin) {
    const adminData = createUserData(admin, 'admin');
    saveToDatabase(adminData);
    return adminData;
}
```

### 7. Complexity Control

#### Strategies to Reduce Complexity
- **Use guard clauses** to simplify nested conditions
- **Extract complex logic** to separate functions
- **Early returns** to reduce nesting depth

**Example:**
```javascript
// Bad - deeply nested logic
function processOrder(order) {
    if (order) {
        if (order.items && order.items.length > 0) {
            if (order.customer) {
                if (order.customer.active) {
                    if (order.total > 0) {
                        // Process order...
                    }
                }
            }
        }
    }
}

// Good - using guard clauses
function processOrder(order) {
    if (!order) throw new Error('Order is required');
    if (!order.items || order.items.length === 0) throw new Error('Order must have items');
    if (!order.customer) throw new Error('Order must have customer');
    if (!order.customer.active) throw new Error('Customer is not active');
    if (order.total <= 0) throw new Error('Order total must be positive');

    // Process order...
}
```

### 8. Testability

#### Principles
- **Pure functions** are easier to test
- **Dependency injection** for better testability
- **Avoid static state** in functions

**Example:**
```javascript
// Bad - hard to test due to hardcoded dependencies and static state
function getCurrentDate() {
    return new Date(); // Hard to test - always returns current date
}

function calculateDiscount(price) {
    const DISCOUNT_RATE = 0.1; // Hardcoded constant
    return price * (1 - DISCOUNT_RATE);
}

// Good - easier to test
function getCurrentDate(currentDate = new Date()) {
    return currentDate; // Can be injected for testing
}

function calculateDiscount(price, discountRate = 0.1) {
    return price * (1 - discountRate);
}
```

### 9. Design Patterns

#### Common Patterns
- **Factory pattern** for object creation
- **Strategy pattern** for interchangeable algorithms
- **Observer pattern** for event handling
- **Dependency injection** for loose coupling

### 10. Magic Numbers and Hardcoding

#### Best Practices
- **Use named constants** instead of magic numbers
- **Externalize configuration** to config files
- **Use environment variables** for environment-specific values

**Example:**
```javascript
// Bad - magic numbers
function calculateShipping(weight) {
    return weight * 2.5 + 10; // 2.5 and 10 are magic numbers
}

// Good - named constants
const SHIPPING_RATE_PER_KG = 2.5;
const BASE_SHIPPING_FEE = 10;

function calculateShipping(weight) {
    return weight * SHIPPING_RATE_PER_KG + BASE_SHIPPING_FEE;
}
```

## Language-Specific Guidelines

### JavaScript/TypeScript
- Use `const` and `let` appropriately (prefer `const`)
- Prefer arrow functions for simple functions
- Use template literals for string concatenation
- Follow ESLint rules and conventions

### Python
- Follow PEP 8 style guidelines
- Use type hints for better code clarity
- Prefer list comprehensions for simple operations
- Use context managers for resource management
- Use f-strings for string formatting

## Code Quality Metrics

### Function Complexity
- **Lines of code**: < 20 lines per function
- **Parameters**: < 4 parameters per function
- **Cyclomatic complexity**: < 10
- **Cognitive complexity**: < 15

### Class Design
- **Number of methods**: < 10 methods per class
- **Class length**: < 300 lines
- **Coupling**: Low coupling between classes

### File Organization
- **File length**: < 500 lines
- **Number of classes**: < 3 classes per file
- **Clear separation of concerns**