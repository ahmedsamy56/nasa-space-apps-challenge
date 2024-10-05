using Blog.Entities.Models;
using Blog.Entities.Repositories;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using System.Security.Claims;

namespace Blog.Web.Areas.Forum.Controllers
{
    [Area("Forum")]
    public class ForumController : Controller
    {
        private readonly IUnitOfWork _unitOfWork;
        public ForumController(IUnitOfWork unitOfWork)
        {
            _unitOfWork = unitOfWork;
        }
        [HttpGet]
        public IActionResult Create()
        {
            return View();
       
        }

        [HttpPost]
        [Authorize]
        public IActionResult Create(ForumTopic forumTopic)
        {
            if (ModelState.IsValid)
            {
                forumTopic.applicationUserId = User.FindFirstValue(ClaimTypes.NameIdentifier);
                _unitOfWork.ForumTopic.Add(forumTopic);
                _unitOfWork.Complete();
                return RedirectToAction(nameof(Index) , "Home");
            }
            return View(forumTopic);
        }

        public IActionResult AddReply(int postId, string text)
        {
            string UserId = User.FindFirstValue(ClaimTypes.NameIdentifier);

            var forumreply = new ForumReply
            {
                Content = text,
                ForumTopicId = postId,
                applicationUserId = UserId
            };

            _unitOfWork.ForumReply.Add(forumreply);
            _unitOfWork.Complete();

            return Ok();
        }


        [HttpPost]
        public IActionResult DeleteReply(int commentId)
        {
            var Reply = _unitOfWork.ForumReply.GetFirstorDefault(c => c.Id == commentId);

            if (Reply == null)
            {
                return NotFound();
            }

            var claimsIdentity = (ClaimsIdentity)User.Identity;
            var claim = claimsIdentity.FindFirst(ClaimTypes.NameIdentifier);
            string userId = claim.Value;

            if (Reply.applicationUserId != userId)
            {
                return Unauthorized();
            }

            _unitOfWork.ForumReply.Remove(Reply);
            _unitOfWork.Complete();

            return Ok();
        }



        public IActionResult DeleteForum(int questionId)
        {
            var question = _unitOfWork.ForumTopic.GetFirstorDefault(c => c.Id == questionId);
            if (question == null)
            {
                return NotFound();
            }
            var claimsIdentity = (ClaimsIdentity)User.Identity;
            var claim = claimsIdentity.FindFirst(ClaimTypes.NameIdentifier);
            string userId = claim.Value;
            if (question.applicationUserId != userId)
            {
                return Unauthorized();
            }

            _unitOfWork.ForumTopic.Remove(question);
            _unitOfWork.Complete();

            return Ok();
        }

    }
}
