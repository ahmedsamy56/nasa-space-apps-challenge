using Blog.DataAccess.Data;
using Blog.Entities.Models;
using Blog.Utilities;
using Microsoft.AspNetCore.Identity;
using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.Logging;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Text;
using System.Threading.Tasks;

namespace Blog.DataAccess.DbInitializer
{
    public class DbInitializer : IDbInitializer
    {
        private readonly UserManager<IdentityUser> _userManager;
        private readonly RoleManager<IdentityRole> _roleManager;
        private readonly AppDbContext _context;

        public DbInitializer(
             AppDbContext context,
            UserManager<IdentityUser> userManager,
            RoleManager<IdentityRole> roleManager)
        {
            _userManager = userManager;
            _roleManager = roleManager;
            _context = context; 
        }
        public void Initialize()
        {
            //migration 
            try
            {
                if (_context.Database.GetPendingMigrations().Count() > 0) 
                {
                    _context.Database.Migrate();
                }


            }
            catch (Exception)
            {
                throw;
            }

            //Roles
            if (!_roleManager.RoleExistsAsync(SD.AdminRole).GetAwaiter().GetResult())
            {
                _roleManager.CreateAsync(new IdentityRole(SD.AdminRole)).GetAwaiter().GetResult();
                _roleManager.CreateAsync(new IdentityRole(SD.EditorRole)).GetAwaiter().GetResult();
                _roleManager.CreateAsync(new IdentityRole(SD.VisitorRole)).GetAwaiter().GetResult();

                //Admin create

                _userManager.CreateAsync(new applicationUser
                {
                    Name = "First Admin",
                    UserName = "Admin@Admin.com",
                    Email = "Admin@Admin.com",
                    Address = "Egypt",

                } , "Pass@12345").GetAwaiter().GetResult();

                applicationUser user = _context.applicationUsers.FirstOrDefault(u=>u.Email == "Admin@Admin.com");

                _userManager.AddToRoleAsync(user, SD.AdminRole).GetAwaiter().GetResult();

            }

            return;
        }
    }
}
