# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution    
#    Copyright (C) 2010 Smile (<http://www.smile.fr>). All Rights Reserved
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    "name" : "Talend Integration",
    "version" : "1.0",
    "author" : "Smile",
    "website": 'http://www.smile.fr',
    "category" : "Tools",
    "description": """Talend Integration

Give access to:
* Jobs
* Logs
* States
* Flows

Suggestions & Feedback to: corentin.pouhet-brunerie@smile.fr
""",
    "depends" : ['smile_ir_actions_extension'],
    "init_xml" : [],
    "update_xml": [
        'security/talend_integration_security.xml',
        'security/ir.model.access.csv',
        'talend_integration_view.xml',
        'talend_log_view.xml',
    ],
    "demo_xml" : [],
    "installable": True,
    "active": False,
}
