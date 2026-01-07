import time

# HRGenie Logic Engine (Python Port)
# Supports Full Detail Mode, Sub-topic Awareness, and Strict Compliance

TOPICS = {
    "ONBOARDING": "onboarding",
    "LEAVE": "leave",
    "ATTENDANCE": "attendance",
    "BENEFITS": "benefits",
    "POLICIES": "policies",
    "HANDBOOK": "handbook",
    "FAQ": "faq",
    "HELP": "help"
}

KNOWLEDGE_BASE = {
    TOPICS["ONBOARDING"]: {
        "keywords": ["onboarding", "new", "joiner", "start", "first day", "welcome", "process", "join", "induction", "orientation", "probation", "document", "lifecycle"],
        "overview": """**HRGenie:** Employee Onboarding Lifecycle:

1. **Pre-Joining**: Offer acceptance, document submission, and background verification.
2. **Day 1 & Orientation**: Welcome session, IT asset setup, and facility tour.
3. **Role Enablement**: Team introductions, goal setting, and specialized training.
4. **Early Support**: Buddy program assignment and regular manager check-ins.
5. **Probation**: Performance evaluation and confirmation process.

*Please ask if you need specific details on any stage.*""",
        "subTopics": [
            {
                "triggers": ["pre-joining", "pre joining", "offer", "document", "background", "before join"],
                "text": """**HRGenie:** 1. Pre-Joining Phase:

• **Offer Formalities**: Ensure you have accepted your formal employment offer.
• **Document Submission**: Submit ID proof, permanent address proof, and education certificates.
• **Background Verification**: We will initiate and complete your background checks.
• **Communications**: Look out for joining instructions sent to your personal email."""
            },
            {
                "triggers": ["day 1", "first day", "orientation", "induction", "it setup", "welcome"],
                "text": """**HRGenie:** 2. Day 1 & Orientation:

• **Welcome Session**: Introduction to company culture, values, and key team members.
• **HR Briefing**: Overview of essential policies, benefits, and compliance.
• **IT Setup**: Configuration of your laptop, email access, and software tools.
• **Office Tour**: A guided tour of the facility and amenities."""
            },
            {
                "triggers": ["role enablement", "training", "team", "manager", "responsibility", "expectations"],
                "text": """**HRGenie:** 3. Role Enablement:

• **Team Introduction**: Meet your reporting manager and direct colleagues.
• **Goal Setting**: Clear expectations and KPIs set for your first 30/60/90 days.
• **Training**: Access to internal learning portals and role-specific tools."""
            },
            {
                "triggers": ["early support", "buddy", "mentor", "feedback", "help", "support"],
                "text": """**HRGenie:** 4. Early Support System:

• **Buddy Program**: Assignment of a peer mentor for daily operational guidance.
• **Manager Check-ins**: Scheduled weekly catch-ups with your reporting manager.
• **Feedback Loop**: Open discussions to ensure you are settling in comfortably."""
            },
            {
                "triggers": ["probation", "confirmation", "performance", "evaluate"],
                "text": """**HRGenie:** 5. Probation Period:

• **Purpose**: To assess mutual fit and performance against set goals.
• **Review Process**: Structured reviews at regular intervals (e.g., 3 months, 6 months).
• **Outcome**: Successful completion leads to employment confirmation."""
            }
        ]
    },
    TOPICS["LEAVE"]: {
        "keywords": ["leave", "vacation", "sick", "holiday", "pto", "casual", "earned", "absent", "time off", "time-off", "maternity", "paternity", "carry forward", "apply"],
        "overview": """**HRGenie:** Leave Policies Overview:

1. **Casual / Personal Leave**: Short-term leave for personal matters.
2. **Sick Leave**: For medical recovery and health issues.
3. **Earned / Paid Leave**: For planned vacations (accrual based).
4. **Public Holidays**: National and Festival holidays.
5. **Special Leaves**: Maternity, Paternity, and Bereavement.
6. **Applying for Leave**: Use the HR Portal.
7. **Approval Process**: Manager approval required.
8. **Carry Forward Rules**: Limits on EL carry-over at year-end.

*Please ask about a specific leave type for details.*""",
        "subTopics": [
            {
                "triggers": ["casual", "personal", "urgent", "cl"],
                "text": """**HRGenie:** 1. Casual / Personal Leave:

• **Purpose**: For personal errands, urgent matters, or unforeseen work.
• **Duration**: Typically used for short durations (1-2 days).
• **Planning**: Please check with your manager in advance whenever possible."""
            },
            {
                "triggers": ["sick", "medical", "ill", "doctor"],
                "text": """**HRGenie:** 2. Sick Leave (SL):

• **Purpose**: For recovery when you are unwell.
• **Documentation**: Medical certificate is required for absences of 3 or more days.
• **Reporting**: Inform your manager regarding your absence as soon as possible."""
            },
            {
                "triggers": ["earned", "paid", "vacation", "el", "pl", "annual"],
                "text": """**HRGenie:** 3. Earned / Paid Leave (EL):

• **Purpose**: For planned long vacations and personal time off.
• **Accrual**: These leaves are earned based on the number of days worked.
• **Planning**: Apply well in advance to assist with team resource planning."""
            },
            {
                "triggers": ["holiday", "public", "festival"],
                "text": """**HRGenie:** 4. Public Holidays:

• The company observes standard National and Festival holidays.
• Please refer to the Intranet Calendar for the current year's complete list."""
            },
            {
                "triggers": ["maternity", "paternity", "bereavement", "special"],
                "text": """**HRGenie:** 5. Special Leaves:

• **Maternity/Paternity**: Provided as per statutory laws and company policy.
• **Bereavement**: Available in the unfortunate event of losing an immediate family member.
• *Note: Contact HR directly for specific eligibility and application details.*"""
            },
            {
                "triggers": ["apply", "portal", "request", "approval", "carry forward"],
                "text": """**HRGenie:** 6-8. Application & Administration:

• **Applying**: All leaves must be applied for via the HR Web Portal.
• **Approval**: Your reporting manager must approve the leave request.
• **Carry Forward**: Up to a limited number of Earned Leave days can be carried forward to the next year (check Handbook)."""
            }
        ]
    },
    TOPICS["ATTENDANCE"]: {
        "keywords": ["attendance", "hour", "working", "time", "late", "shift", "check-in", "clock", "present", "entry", "remote", "hybrid", "wfh", "absent", "tracking", "compliance"],
        "overview": """**HRGenie:** Attendance Rules:

1. **Working Hours / Shifts**: Standard timings and flexibility.
2. **Attendance Tracking**: Biometric and portal-based logging.
3. **Late Arrival / Early Departure**: Reporting and grace periods.
4. **Absence Reporting**: Protocols for planned and unplanned leave.
5. **Remote / Hybrid Work**: WFH guidelines and logging.
6. **General Compliance**: Punctuality and accountability.""",
        "subTopics": [
            {
                "triggers": ["shift", "hour", "time", "9", "6", "standard", "flexi"],
                "text": """**HRGenie:** 1. Working Hours / Shifts:

• **Standard Timings**: 9:00 AM to 6:00 PM (Monday to Friday).
• **Flexible Hours**: Available upon discussion with your manager, subject to role requirements.
• **Core Hours**: Employees are expected to be available during core business hours (11:00 AM - 4:00 PM)."""
            },
            {
                "triggers": ["mark", "check", "biometric", "portal", "log", "track"],
                "text": """**HRGenie:** 2. Attendance Tracking:

• **Biometric**: Use the scanners at entry/exit points in the office.
• **Online Check-in**: Use the HR Web Portal for remote logging (if enabled).
• **Responsibility**: It is your personal responsibility to ensure daily attendance is marked correctly."""
            },
            {
                "triggers": ["late", "start", "delay", "early", "departure"],
                "text": """**HRGenie:** 3. Late Arrival / Early Departure:

• **Reporting**: Inform your manager immediately if you anticipate being more than 15 minutes late.
• **Impact**: Frequent lateness or early departures may impact performance reviews.
• **Correction**: Missed swipes must be regularized within 24 hours."""
            },
            {
                "triggers": ["absence", "reporting", "inform"],
                "text": """**HRGenie:** 4. Absence Reporting:

• **Unplanned**: Notify your manager by 9:30 AM via email or text.
• **Planned**: Apply for leave in advance via the portal.
• **No-Show**: Unreported absence for 3 days may be treated as abandonment."""
            },
            {
                "triggers": ["wfh", "remote", "hybrid", "home"],
                "text": """**HRGenie:** 5. Remote / Hybrid Work:

• **Policy**: Remote work is permissible based on team agreement and role suitability.
• **Logging**: Remote hours must be logged via the specific Remote Module.
• **Availability**: Ensure you are reachable via Teams/Email during agreed working hours."""
            },
             {
                "triggers": ["compliance", "punctuality", "rule"],
                "text": """**HRGenie:** 6. General Compliance:

• **Punctuality**: Timely attendance ensures smooth team operations.
• **Accountability**: You are accountable for your logged hours.
• **Integrity**: Any discrepancy in logging should be reported to HR immediately."""
            }
        ]
    },
    TOPICS["BENEFITS"]: {
        "keywords": ["benefit", "insurance", "health", "perk", "gym", "bonus", "incentive", "welfare", "support", "learning", "allowance", "wellness", "reward", "mentor"],
        "overview": """**HRGenie:** Employee Benefits:

1. **Health & Insurance**: Medical, Dental, and Vision coverage.
2. **Wellness Programs**: Mental health, fitness, and stress management.
3. **Paid Time Off**: Vacation, Personal, and Sick leave.
4. **Incentives & Rewards**: Performance bonuses and recognition.
5. **Learning & Development**: Training and certifications.
6. **Mentorship Programs**: Leadership guidance.
7. **Employee Support Programs**: Counseling and grievances.""",
        "subTopics": [
            {
                "triggers": ["insurance", "health", "medical", "life", "dental", "vision"],
                "text": """**HRGenie:** 1. Health & Insurance:

• **Medical Insurance**: Covers hospitalization for self and immediate dependents.
• **Dental & Vision**: Basic coverage provided as part of the wellness plan (overview only).
• **Term Life**: Coverage provided for unfortunate events.
• *Refer to the specific policy document for coverage limits.*"""
            },
            {
                "triggers": ["wellness", "mental", "counseling", "gym", "fitness", "stress"],
                "text": """**HRGenie:** 2. Wellness Programs:

• **Mental Health**: Access to confidential support and counseling services.
• **Fitness**: Corporate memberships or discounts for fitness programs.
• **Stress Management**: Regular workshops and sessions on well-being."""
            },
             {
                "triggers": ["paid time off", "pto"],
                "text": """**HRGenie:** 3. Paid Time Off:

• Refer to the **Leave Policies** section for details on Casual, Sick, and Earned leaves."""
            },
             {
                "triggers": ["incentive", "bonus", "reward", "performance"],
                "text": """**HRGenie:** 4. Incentives & Rewards:

• **Performance Bonus**: Annual variable pay based on company and individual performance.
• **Recognition**: Spot awards for exceptional contributions.
• *Note: Specific eligibility is based on your offer letter.*"""
            },
             {
                "triggers": ["learning", "course", "certification", "training", "development"],
                "text": """**HRGenie:** 5. Learning & Development:

• **Internal Training**: Access to our Learning Management System (LMS).
• **Certifications**: Support for role-relevant professional certifications.
• **Seminars**: Opportunities to attend industry conferences."""
            },
            {
                "triggers": ["mentor", "leadership", "guidance"],
                "text": """**HRGenie:** 6. Mentorship Programs:

• **Internal Mentors**: Connect with senior leaders for career guidance.
• **Peer Coaching**: Learning from experienced colleagues."""
            },
             {
                "triggers": ["support", "grievance", "hr support"],
                "text": """**HRGenie:** 7. Employee Support Programs:

• **Counseling**: Professional counseling available via EAP.
• **HR Support**: Dedicated HR Business Partners for query resolution.
• **Grievance**: Formal mechanisms to address workplace concerns confidentially."""
            }
        ]
    },
    TOPICS["POLICIES"]: {
        "keywords": ["policies", "policy", "hr policies", "rule", "guideline"],
        "overview": """**HRGenie:** HR Policies Hub:

I can explain the following policies:
1. **Onboarding**: From joining to probation completion.
2. **Leave**: Types of leave and application rules.
3. **Attendance**: Work hours, remote work, and tracking.
4. **Benefits**: Insurance, wellness, and rewards.
5. **Ethics**: Code of conduct and safety guidelines.

*Please ask about a specific topic for more details.*""",
        "subTopics": []
    },
    TOPICS["HANDBOOK"]: {
        "keywords": ["handbook", "code", "conduct", "harassment", "behavior", "ethics", "integrity", "safety", "it usage", "security", "compliance"],
        "overview": """**HRGenie:** Ethics, Safety & IT:

1. **Integrity & Confidentiality**: Honesty and data protection.
2. **Safety Guidelines**: Zero tolerance for harassment, POSH, and emergencies.
3. **IT Usage Policies**: Device and software usage rules.""",
        "subTopics": [
             {
                "triggers": ["ethics", "integrity", "confidentiality", "privacy"],
                "text": """**HRGenie:** 1. Integrity & Confidentiality:

• **Honesty**: Always act with integrity in all business dealings.
• **Data Privacy**: Strictly protect client and company proprietary data.
• **Conflict of Interest**: Disclose any outside interests that may conflict with work."""
            },
             {
                "triggers": ["it", "computer", "laptop", "software", "password", "security"],
                "text": """**HRGenie:** 3. IT Usage Policies:

• **Device Usage**: Laptops are for business purposes only.
• **Access Control**: Never share your passwords.
• **Software Policy**: Do not install unauthorized applications."""
            },
            {
                "triggers": ["safety", "emergency", "fire", "harassment", "posh"],
                "text": """**HRGenie:** 2. Safety Guidelines:

• **POSH**: We maintain a zero-tolerance approach to harassment.
• **Emergency**: Familiarize yourself with fire exit routes and assembly points.
• **Reporting**: Contact HR immediately regarding any unsafe conditions or behavior."""
            }
        ]
    },
     TOPICS["FAQ"]: {
        "keywords": ["faq", "frequently asked questions", "question"],
        "overview": """**HRGenie:** Frequently Asked Questions:

1. **Documents**: ID, Address proof, and Educational certificates needed.
2. **Reporting Time**: Standard reporting time is 9:00 AM.
3. **Leave Application**: Use the HR Portal to apply.
4. **Insurance**: Coverage is active from your date of joining.

*For more queries, please ask specific questions.*""",
        "subTopics": []
    },
    TOPICS["HELP"]: {
        "keywords": ["help", "support", "assist", "need help"],
        "overview": """**HRGenie:** Help & Assistance:

**I can assist you with:**
• Onboarding processes
• HR Policies (Leave, Attendance)
• Employee Benefits

**I cannot assist with:**
• Approving or rejecting leaves (Please ask your manager)
• Payroll or salary calculations
• Making HR decisions

*Please type your question to proceed.*""",
        "subTopics": []
    }
}

RESTRICTED_TOPICS = [
    {
        "keywords": ["approve", "reject", "permission", "allow"],
        "response": """**HRGenie:** I cannot fulfill this request.
I can explain the relevant policy, but **approvals must come from your manager** or the HR department.
Please use the appropriate portal for requests."""
    },
    {
        "keywords": ["salary", "bonus", "pay", "raise", "payroll", "bank", "account", "compensation"],
        "response": """**HRGenie:** I do not have access to this information.
I cannot view **personal financial data** or manage payroll.
Please contact the Payroll Team directly."""
    },
    {
        "keywords": ["legal", "law", "sue", "complaint", "harassment", "grievance"],
        "response": """**HRGenie:** I cannot provide legal advice.
For serious issues, **please contact HR Confidential** or the Legal department immediately."""
    }
]

def find_topic(query):
    lower_query = query.lower()
    for key, data in KNOWLEDGE_BASE.items():
        if any(k in lower_query for k in data["keywords"]):
            return key
    return None

def process_query(query, last_topic=None):
    # Simulate thinking time
    time.sleep(0.6)
    
    lower_query = query.lower()
    
    # 1. Check Restrictions
    for restriction in RESTRICTED_TOPICS:
        if any(k in lower_query for k in restriction["keywords"]):
            return {"text": restriction["response"], "topic": last_topic}

    # 2. Context Aware Check (Follow-up)
    if last_topic and last_topic in KNOWLEDGE_BASE:
        topic_data = KNOWLEDGE_BASE[last_topic]
        if "subTopics" in topic_data:
            for sub in topic_data["subTopics"]:
                if any(t in lower_query for t in sub["triggers"]):
                    return {"text": sub["text"], "topic": last_topic}

    # 3. New Topic Detection
    new_topic = find_topic(query)
    if new_topic:
        topic_data = KNOWLEDGE_BASE[new_topic]
        
        # Check if initial query is a sub-topic
        if "subTopics" in topic_data:
            for sub in topic_data["subTopics"]:
                if any(t in lower_query for t in sub["triggers"]):
                    return {"text": sub["text"], "topic": new_topic}
        
        return {"text": topic_data["overview"], "topic": new_topic}

    # 4. Fallback
    return {
        "text": "Sorry boss, this is not in our work, but I can help you with work related to onboarding and HR policies.",
        "topic": last_topic
    }
